#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017-2020  The Project X-Ray Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

import argparse
from collections import namedtuple
import progressbar
import capnp
import capnp.lib.capnp
capnp.remove_import_hook()
import math
import sys

from distributed_bsc import BipartiteAdjacencyMatrix, find_bsc_par, \
        greedy_set_cover_with_complete_bipartite_subgraphs, \
        greed_set_cover_par
import gc
import multiprocessing
from reference_model import CompactArray, StructOfArray
import os.path

from node_lookup import NodeLookup

Tile = namedtuple('Tile', 'tile_pkey')
WireToNode = namedtuple(
    'WireToNode', 'wire_in_tile_pkey delta_x delta_y node_wire_in_tile_pkey')
NodeToWire = namedtuple('NodeToWire', 'wire_in_tile_pkey delta_x delta_y')


def get_wire_to_node_graph(database, tile_type):

    lookup = NodeLookup(database=database)
    cur = lookup.conn.cursor()
    cur2 = lookup.conn.cursor()
    cur3 = lookup.conn.cursor()

    all_tiles = set()
    all_wire_to_nodes = set()

    graph = BipartiteAdjacencyMatrix()

    #### Get tile type pkey
    cur.execute("SELECT pkey FROM tile_type WHERE name = ?;", (tile_type, ))
    tile_type_pkey = cur.fetchone()[0]

    #BEN Get all the tiles of a type
    for tile_pkey, tile_type_pkey, tile_name, tile_x, tile_y in progressbar.progressbar(
            cur.execute(
                "SELECT pkey, tile_type_pkey, name, x, y FROM tile WHERE tile_type_pkey = ?;",
                (tile_type_pkey, ))):

        tile = Tile(tile_pkey=tile_pkey)
        graph.add_u(tile)
        all_tiles.add(tile)

        #BEN Get all physical wires in this tile
        for wire_in_tile_pkey, wire_pkey, node_pkey in cur2.execute("""
SELECT wire_in_tile_pkey, wire.pkey, wire.node_pkey
FROM wire
WHERE tile_pkey = ?;
                """, (tile_pkey, )):
            #BEN Grab the home location of this wire's node_source_wire
            cur3.execute(
                """
SELECT tile.x, tile.y, node.wire_in_tile_pkey
FROM node
INNER JOIN tile ON node.tile_pkey = tile.pkey
WHERE node.pkey = ?;
                """, (node_pkey, ))
            node_tile_x, node_tile_y, node_wire_in_tile_pkey = cur3.fetchone()

            delta_x = node_tile_x - tile_x
            delta_y = node_tile_y - tile_y

            if delta_x == 0 and delta_y == 0 and wire_in_tile_pkey == node_wire_in_tile_pkey:
                continue

            pattern = WireToNode(
                wire_in_tile_pkey=wire_in_tile_pkey,
                delta_x=delta_x,
                delta_y=delta_y,
                node_wire_in_tile_pkey=node_wire_in_tile_pkey)

            if pattern not in all_wire_to_nodes:
                all_wire_to_nodes.add(pattern)
                graph.add_v(pattern)

            graph.add_edge(tile, pattern)

    graph.build()

    return graph

#############################################################################################
#############################################################################################

#BEN 
# Build a bi-partite graph.  
# The u's are all the tiles of the given type
# The v's consist of nodes in those tiles paired with the wires in them which are in other tiles (in the case of --pips_only they are wires
#   that drive PIPs in other tiles)
# Thus, for a given tile there will be one or more node entries and for each node entry there will be one or more wires
# When done, the graph will have u_to_v and v_to_u bitmaps showing which tiles go with which node_to_wires records and vice versa
# That is it.
def get_node_to_wires_graph(database, tile_type, only_pips):
    lookup = NodeLookup(database=database)
    cur = lookup.conn.cursor()
    cur2 = lookup.conn.cursor()
    cur3 = lookup.conn.cursor()

    all_tiles = set()
    all_node_to_wires = set()

    graph = BipartiteAdjacencyMatrix()

    cur.execute("SELECT pkey FROM tile_type WHERE name = ?;", (tile_type, ))
    tile_type_pkey = cur.fetchone()[0]

    print("Tile type pkey = {}, only_pips = {}".format(tile_type_pkey, only_pips))    #BEN

    if only_pips:
        extra_conditions = " AND wire_in_tile.has_pip_from"
    else:
        extra_conditions = ""

    tcnt = 0  #BEN
    #BEN For every tile of the specified type
    for tile_pkey, tile_type_pkey, tile_name, tile_x, tile_y in progressbar.progressbar(
            cur.execute(
                "SELECT pkey, tile_type_pkey, name, x, y FROM tile WHERE tile_type_pkey = ?;",
                (tile_type_pkey, ))):
        print("  Looking at tile: {}, {}, {}, {}/{}".format(
            tile_pkey, tile_type_pkey, tile_name, tile_x, tile_y))   ####
        tcnt += 1 #BEN
        #BEN Create object for tile and add it to the graph and all_tiles list
        tile = Tile(tile_pkey=tile_pkey)
        graph.add_u(tile)
        all_tiles.add(tile)

        #BEN For every node who starts in this tile
        nwit = 0   ####
        for node_pkey, node_wire_in_tile_pkey in cur2.execute("""
SELECT node.pkey, node.wire_in_tile_pkey
FROM node
WHERE node.tile_pkey = ?;
            """, (tile_pkey, )):

            #print(f"    Looking at node: node= {node_pkey} node_wire_in_tile= {node_wire_in_tile_pkey}")
            nwit += 1;  #BEN
            node_to_wires = []

            #BEN The next set of lines get a list of wires in this node (optional: that drive PIPs in other tiles)
            for wire_pkey, wire_in_tile_pkey, wire_tile_x, wire_tile_y in cur3.execute("""
SELECT wire.pkey, wire.wire_in_tile_pkey, tile.x, tile.y
FROM wire
INNER JOIN tile ON wire.tile_pkey = tile.pkey
INNER JOIN wire_in_tile ON wire.wire_in_tile_pkey = wire_in_tile.pkey
WHERE wire.node_pkey = ? {};
                """.format(extra_conditions), (node_pkey, )):

                delta_x = wire_tile_x - tile_x
                delta_y = wire_tile_y - tile_y

                ###print("        Processing wire:  node = {}  wire= {} witpk= {} x= {}, y= {}   nwit= {}".format(
                ###    node_pkey, wire_pkey, wire_in_tile_pkey, wire_tile_x, wire_tile_y, node_wire_in_tile_pkey)
                ###    )
                #BEN If: in same tile and wire is node's source wire THEN ignore
                if delta_x == 0 and delta_y == 0 and wire_in_tile_pkey == node_wire_in_tile_pkey:
                    continue
                ###print("            Appending:  {} {} {},{}".format(
                ###    node_pkey, wire_in_tile_pkey, delta_x, delta_y)
                ###    )

                node_to_wires.append(
                    NodeToWire(
                        delta_x=delta_x,
                        delta_y=delta_y,
                        wire_in_tile_pkey=wire_in_tile_pkey))

            if len(node_to_wires) == 0:
                continue

            node_to_wires = (node_wire_in_tile_pkey, frozenset(node_to_wires))
            if node_to_wires not in all_node_to_wires:
                all_node_to_wires.add(node_to_wires)
                graph.add_v(node_to_wires)

            graph.add_edge(tile, node_to_wires)
        ###print("         Total nodes in tile = {}".format(nwit))
    print("      Total tiles = {}".format(tcnt))    ####

    #BEN
    #print("Printing graph at this point")
    #print(f"Graph has tiles: {graph.u}")
    #for v in graph.v:
    #    print(f"  Node in this tile is : {v[0]}")
    #    print(f"    It has in it a wire driving a PIP (at another tile): {v[1]}")

    
    #BEN Build a bitmaps reflecting which tile is associated with each node_to_wire and the other way around
    graph.build()
    return graph

#############################################################################################
#############################################################################################

def write_wire_to_node(
        graph, required_solutions, tile_patterns, tile_to_tile_patterns,
        output_dir, tile_type):
    wire_in_tile_pkeys = set()
    all_node_patterns = set()

    for pattern in graph.v:
        wire_in_tile_pkeys.add(pattern.wire_in_tile_pkey)
        all_node_patterns.add(
            (pattern.delta_x, pattern.delta_y, pattern.node_wire_in_tile_pkey))

    wire_in_tile_pkeys_data = CompactArray()
    wire_in_tile_pkeys_data.set_items(sorted(wire_in_tile_pkeys))

    node_patterns = StructOfArray(
        'WireToNodePattern', ('delta_x', 'delta_y', 'node_wire_in_tile_pkey'))
    node_patterns.set_items(sorted(all_node_patterns))

    subgraphs = []
    subgraphs_null_count = []
    subgraph_idx_to_tiles = {}

    for subgraph_idx, (tiles, patterns) in enumerate(required_solutions):
        subgraph_idx_to_tiles[subgraph_idx] = tiles

        subgraph = CompactArray()
        subgraph.init_items(len(wire_in_tile_pkeys))

        for pattern in patterns:
            idx = wire_in_tile_pkeys_data.index(pattern.wire_in_tile_pkey)
            subgraph.items[idx] = node_patterns.index(
                (
                    pattern.delta_x, pattern.delta_y,
                    pattern.node_wire_in_tile_pkey))

        null_count = 0
        for item in subgraph.items:
            if item is None:
                null_count += 1

        subgraphs.append(subgraph)
        subgraphs_null_count.append(null_count)

    tile_patterns_data = []
    tile_pattern_to_index = {}
    tile_patterns = sorted(tile_patterns)
    for idx, tile_pattern in enumerate(tile_patterns):
        tile_pattern_to_index[tile_pattern] = idx
        tile_pattern_data = CompactArray()

        # Have tile patterns put more complete subgraphs earlier than later.
        tile_pattern_data.set_items(
            sorted(tile_pattern, key=lambda x: subgraphs_null_count[x]))
        tile_patterns_data.append(tile_pattern_data)

    tile_to_tile_patterns_data = []
    for tile, tile_pattern in tile_to_tile_patterns.items():
        tile_pattern_index = tile_pattern_to_index[tile_pattern]
        tile_to_tile_patterns_data.append((tile.tile_pkey, tile_pattern_index))

        for subgraph_idx in tile_patterns[tile_pattern_index]:
            assert tile in subgraph_idx_to_tiles[subgraph_idx]

            subgraph = subgraphs[subgraph_idx]

            for wire_idx, node_pattern_idx in enumerate(subgraph.items):
                if node_pattern_idx is None:
                    continue

                wire_in_tile_pkey = wire_in_tile_pkeys_data.items[wire_idx]
                pattern = node_patterns.get(node_pattern_idx)

                pattern_tup = WireToNode(
                    wire_in_tile_pkey=wire_in_tile_pkey,
                    delta_x=pattern['delta_x'],
                    delta_y=pattern['delta_y'],
                    node_wire_in_tile_pkey=pattern['node_wire_in_tile_pkey'],
                )

                assert graph.is_edge(tile, pattern_tup)

    tile_to_tile_patterns = StructOfArray(
        'TileToTilePatterns', ('tile_pkey', 'tile_pattern_index'))
    tile_to_tile_patterns.set_items(sorted(tile_to_tile_patterns_data))

    graph_storage_schema = capnp.load('graph_storage.capnp')
    wire_to_nodes = graph_storage_schema.WireToNodeStorage.new_message()

    #BEN
    print("Wire_in_tile_pkeys: (len= {})".format(len(wire_in_tile_pkeys)))
    print(wire_in_tile_pkeys)
    wire_in_tile_pkeys_data.write_to_capnp(wire_to_nodes.wireInTilePkeys)

    #BEN
    print("Node patterns, len={}".format(len(node_patterns.items[0].items)))
    for idx, rec in enumerate(zip(node_patterns.items[0].items, node_patterns.items[1].items, node_patterns.items[2].items)):
        print("[{}]   {}  {}, {}".format(idx, rec[2], rec[0], rec[1]))
    node_patterns.write_to_capnp(
        (
            wire_to_nodes.nodePatternDx,
            wire_to_nodes.nodePatternDy,
            wire_to_nodes.nodePatternToNodeWire,
        ))

    #BEN
    print("Subgraphs: (len = {})".format(len(subgraphs)))
    for idx, subgraph in enumerate(subgraphs):
        print("  Subgraph[{}], len={} \n     {}".format(idx, len(subgraph.items), subgraph.items))
    subgraphs_capnp = wire_to_nodes.init('subgraphs', len(subgraphs))
    for subgraph_capnp, subgraph in zip(subgraphs_capnp, subgraphs):
        subgraph.write_to_capnp(subgraph_capnp)

    #BEN
    print("Tile_patterns_data:   len={}".format(len(tile_patterns_data)))
    for tpd in tile_patterns_data:
        print("  ",  tpd.items)
    tile_patterns_capnp = wire_to_nodes.init(
        'tilePatterns', len(tile_patterns_data))
    for tile_pattern_capnp, tile_pattern in zip(tile_patterns_capnp,
                                                tile_patterns_data):
        tile_pattern.write_to_capnp(tile_pattern_capnp)

    #BEN
    print("Tile_to_tile_patterns:   len={}".format(len(tile_to_tile_patterns.items)))
    for tttp in tile_to_tile_patterns.items:
        print("  ", tttp.items)
    tile_to_tile_patterns.write_to_capnp(
        (wire_to_nodes.tilePkeys, wire_to_nodes.tileToTilePatterns))

    serialized = wire_to_nodes.to_bytes()
    print('Size on disk: ', len(serialized))
    if output_dir:
        with open(os.path.join(output_dir,
                               '{}_wire_to_nodes.bin'.format(tile_type)),
                  'wb') as f:
            f.write(serialized)


def write_node_to_wires(
        graph, required_solutions, tile_patterns, tile_to_tile_patterns,
        output_dir, tile_type, only_pips):
    node_wire_in_tile_pkeys = set()
    all_wire_patterns = set()

    for node_wire_in_tile_pkey, node_to_wires in graph.v:
        node_wire_in_tile_pkeys.add(node_wire_in_tile_pkey)

        for pattern in node_to_wires:
            all_wire_patterns.add(
                (pattern.delta_x, pattern.delta_y, pattern.wire_in_tile_pkey))

    node_wire_in_tile_pkeys_array = CompactArray()
    node_wire_in_tile_pkeys_array.set_items(sorted(node_wire_in_tile_pkeys))

    wire_patterns = StructOfArray(
        "NodeToWirePattern", ('delta_x', 'delta_y', 'wire_in_tile_pkey'))
    wire_patterns.set_items(sorted(all_wire_patterns))

    node_patterns_to_idx = {}
    node_patterns_data = []
    for _, node_patterns in required_solutions:
        for _, patterns in node_patterns:
            if patterns in node_patterns_to_idx:
                continue

            node_patterns_to_idx[patterns] = len(node_patterns_data)
            node_patterns_data.append(CompactArray())

            node_patterns = []
            for pattern in patterns:
                key = (
                    pattern.delta_x, pattern.delta_y,
                    pattern.wire_in_tile_pkey)
                assert key in all_wire_patterns
                node_patterns.append(wire_patterns.index(key))
            node_patterns_data[-1].set_items(sorted(node_patterns))

    subgraphs = []
    subgraphs_null_count = []

    for tile_pkeys, node_patterns in required_solutions:
        subgraph = CompactArray()
        subgraph.init_items(len(node_wire_in_tile_pkeys))

        for node_wire_in_tile_pkey, node_patterns in node_patterns:
            idx = node_wire_in_tile_pkeys_array.index(node_wire_in_tile_pkey)
            subgraph.items[idx] = node_patterns_to_idx[node_patterns]

        null_count = 0
        for item in subgraph.items:
            if item is None:
                null_count += 1

        subgraphs.append(subgraph)
        subgraphs_null_count.append(null_count)

    tile_patterns_data = []
    tile_pattern_to_index = {}
    for idx, tile_pattern in enumerate(tile_patterns):
        tile_pattern_to_index[tile_pattern] = idx
        tile_pattern_data = CompactArray()

        # Have tile patterns put more complete subgraphs earlier than later.
        tile_pattern_data.set_items(
            sorted(tile_pattern, key=lambda x: -subgraphs_null_count[x]))
        tile_patterns_data.append(tile_pattern_data)

    tile_to_tile_patterns_data = []
    for tile, tile_pattern in tile_to_tile_patterns.items():
        tile_to_tile_patterns_data.append(
            (tile.tile_pkey, tile_pattern_to_index[tile_pattern]))

    tile_to_tile_patterns = StructOfArray(
        'TileToTilePatterns', ('tile_pkey', 'tile_pattern_index'))
    tile_to_tile_patterns.set_items(sorted(tile_to_tile_patterns_data))

    #BEN node_to_wires contains it all
    # for CLK_PMV with PIPs option:
    #    tilePkeys = 9243
    #    nodeWireInTilePkeys = [8379, 8435, 8463]
    #    wirePatternToWire = [73944, 73952, 73956]
    #    wirePatternDx = [-1, -1, -1]
    #    wirePatternDy = [-3, -3, -3]
    #BEN This says that there is a single tile of CLK_PMV type (9243)
    #     It has 3 nodes in which contain wires that drive PIPs in other tiles (8379, ...)
    #     Foreach such node, the relevant wires are given along dx, dy offsets to the other tiles
    graph_storage_schema = capnp.load('graph_storage.capnp')
    node_to_wires = graph_storage_schema.NodeToWiresStorage.new_message()

    #BEN Wires in node that drive PIPs in other tiles

    if node_wire_in_tile_pkeys_array.item_to_idx:
        print("Printing node_wire_tile_pkeys_array: len=", len(node_wire_in_tile_pkeys_array.item_to_idx))
        for itm in node_wire_in_tile_pkeys_array.item_to_idx:
            print("  ", node_wire_in_tile_pkeys_array.item_to_idx[itm], itm)
    else:
        print("*** node_wire_tile_pkeys_array is empty...")
    node_wire_in_tile_pkeys_array.write_to_capnp(
        node_to_wires.nodeWireInTilePkeys)

    #BEN
    print("Wire patterns:  len=", len(wire_patterns.items[0].items))
    assert(len(wire_patterns.items[0].items) == len(wire_patterns.items[1].items))
    assert(len(wire_patterns.items[0].items) == len(wire_patterns.items[2].items))
    for idx,itm in enumerate(zip( wire_patterns.items[0].items, 
                    wire_patterns.items[1].items, 
                    wire_patterns.items[2].items)):
        print("   {} {} {}, {}".format(idx, itm[2], itm[0], itm[1]))

    wire_patterns.write_to_capnp(
        (
            #BEN dx's, dy's, and wires of patterns as in [-1, -1, -1], [-3, -3, -3], [73944, 73952, 73956]
            node_to_wires.wirePatternDx,
            node_to_wires.wirePatternDy,
            node_to_wires.wirePatternToWire,
        ))

    #BEN 
    print("Node_patterns_data:  len=", len(node_patterns_data))
    for idx, npd in enumerate(node_patterns_data):
        print("  {} {}".format(idx, npd.items))
    node_patterns_capnp = node_to_wires.init(
        'nodePatterns', len(node_patterns_data))
    for node_pattern_capnp, node_pattern in zip(node_patterns_capnp,
                                                node_patterns_data):
        node_pattern.write_to_capnp(node_pattern_capnp)

    #BEN
    print("Subgraphs:  len=", len(subgraphs))
    for idx, sg in enumerate(subgraphs):
        print("  {}: {}".format(idx, sg.items))
    subgraphs_capnp = node_to_wires.init('subgraphs', len(subgraphs))
    for subgraph_capnp, subgraph in zip(subgraphs_capnp, subgraphs):
        subgraph.write_to_capnp(subgraph_capnp)

    #BEN
    print("Tile_patterns_data:  len=", len(tile_patterns_data))
    for idx, tpd in enumerate(tile_patterns_data):
        print(" {} {}".format(idx, tpd.items))
    tile_patterns_capnp = node_to_wires.init(
        'tilePatterns', len(tile_patterns_data))
    for tile_pattern_capnp, tile_pattern in zip(tile_patterns_capnp,
                                                tile_patterns_data):
        tile_pattern.write_to_capnp(tile_pattern_capnp)

    #BEN
    print("Tile_to_tile_patterns:  len=", len(tile_to_tile_patterns.items))
    for idx, tttp in enumerate(tile_to_tile_patterns.items):
        print("  {} {}".format(idx, tttp.items))
    tile_to_tile_patterns.write_to_capnp(
        (node_to_wires.tilePkeys, node_to_wires.tileToTilePatterns))

    #BEN Serialize the node_to_wires to disk
    serialized = node_to_wires.to_bytes()
    print('Size on disk: ', len(serialized))
    if output_dir:
        if only_pips:
            fname = '{}_node_to_pip_wires.bin'.format(tile_type)
        else:
            fname = '{}_node_to_wires.bin'.format(tile_type)

        with open(os.path.join(output_dir, fname), 'wb') as f:
            f.write(serialized)

def printBicliques(found_solutions):
    print("There are {} bicliques:".format(len(found_solutions)))
    for s in found_solutions:
        assert len(s) == 2
        print("    s is one biclique and is a tuple (setOfTiles, setOfNodeToWire)")
        print("         Tiles:")
        for t in s[0]:
            print("               {}".format(t))
        print("         NodeToWires:")
        for ntw in s[1]:
            print("               {}".format(ntw))

def reduce_graph(args, all_edges, graph):
    density = graph.density()
    beta = .5
    P = (0.6 - 0.8 * beta) * math.exp((4 + 3 * beta) * density)
    N = 0.01 * len(graph.u) * len(graph.v)

    if args.wire_to_node:
        tile_wire_ids = set()
        wire_nodes = set()
        dxdys = set()
        max_dxdy = 0
        for pattern in graph.v:
            tile_wire_ids.add(pattern.node_wire_in_tile_pkey)
            wire_nodes.add(pattern.wire_in_tile_pkey)
            dxdys.add((pattern.delta_x, pattern.delta_y))
            max_dxdy = max(max_dxdy, abs(pattern.delta_x))
            max_dxdy = max(max_dxdy, abs(pattern.delta_y))

        print('Wire nodes {}'.format(len(wire_nodes)))
        print('Unique node wire in tile pkey {}'.format(len(tile_wire_ids)))
        print('Unique pattern {}'.format(len(graph.v)))
        print('Unique dx dy {}'.format(len(dxdys)))
        print('Unique dx dy dist {}'.format(max_dxdy))
    elif args.node_to_wires:
        tile_wire_ids = set()
        node_wires = set()
        patterns = set()
        dxdys = set()
        max_dxdy = 0
        max_patterns_to_node = 0

        node_to_wires_to_count = {}

        #BEN For each record in graph.v pull out info and store in variety of data structures
        for node_wire_in_tile_pkey, node_to_wires in graph.v:
            # Add node to node_wires set
            node_wires.add(node_wire_in_tile_pkey)

            #BEN Mark how many wires in each
            if node_to_wires not in node_to_wires_to_count:
                node_to_wires_to_count[node_to_wires] = len(node_to_wires)

            #BEN Keep track of biggest one
            max_patterns_to_node = max(
                max_patterns_to_node, len(node_to_wires))
            #BEN For each wire in node_to_wires
            for pattern in node_to_wires:
                patterns.add(pattern)
                tile_wire_ids.add(pattern.wire_in_tile_pkey)
                dxdys.add((pattern.delta_x, pattern.delta_y))
                max_dxdy = max(max_dxdy, abs(pattern.delta_x))
                max_dxdy = max(max_dxdy, abs(pattern.delta_y))

        pattern_count = 0
        max_node_to_wires = 0
        for num_patterns in node_to_wires_to_count.values():
            pattern_count += num_patterns
            max_node_to_wires = max(max_node_to_wires, num_patterns)

        print('Node wires: {}'.format(len(node_wires)))
        print('Max number of patterns: {}'.format(max_node_to_wires))
        print('Minimum number of pattern storage: {}'.format(pattern_count))
        print('Unique wire in tile pkey {}'.format(len(tile_wire_ids)))
        print('Unique node_to_wires {}'.format(len(graph.v)))
        print('Unique patterns {}'.format(len(patterns)))
        print('Unique dx dy {}'.format(len(dxdys)))
        print('Unique dx dy dist {}'.format(max_dxdy))
    else:
        assert False

    print(
        'density = {}, beta = {}, P = {}, N = {}'.format(density, beta, P, N))

    P = math.ceil(P)
    N = math.ceil(N)

    found_solutions, remaining_edges = find_bsc_par(
        num_workers=40, batch_size=100, graph=graph, N=N, P=P)
    assert len(remaining_edges) == 0
    print('Found {} possible complete subgraphs'.format(len(found_solutions)))

    printBicliques(found_solutions)

    required_solutions = greedy_set_cover_with_complete_bipartite_subgraphs(
        all_edges, found_solutions)
    print(
        '{} complete subgraphs required for solution'.format(
            len(required_solutions)))

    required_solutions.sort()

    solution_to_idx = {}
    for idx, solution in enumerate(required_solutions):
        solution_to_idx[solution] = idx

    def get_tile_edges():
        for tile in graph.u:
            edges = set()
            for vj_idx, is_set in enumerate(graph.get_row(tile)):
                if is_set:
                    pattern = graph.v[vj_idx]
                    edges.add((tile, pattern))

            yield tile, edges

    tile_patterns = set()
    tile_to_tile_patterns = {}

    for tile, solutions_for_tile in progressbar.progressbar(
            greed_set_cover_par(num_workers=40,
                                required_solutions=required_solutions,
                                edges_iter=get_tile_edges())):
        tile_pattern = set()
        for solution in solutions_for_tile:
            tile_pattern.add(solution_to_idx[solution])

        tile_pattern = frozenset(tile_pattern)
        tile_to_tile_patterns[tile] = tile_pattern
        tile_patterns.add(tile_pattern)

    number_of_tile_pattern_elements = 0
    for tile_pattern in tile_patterns:
        number_of_tile_pattern_elements += len(tile_pattern)

    print('Have {} tile patterns'.format(len(tile_patterns)))
    print(
        'Max {} patterns'.format(
            max(len(patterns) for patterns in tile_to_tile_patterns.values())))
    print(
        'Number of tile pattern elements: {}'.format(
            number_of_tile_pattern_elements))

    return required_solutions, tile_patterns, tile_to_tile_patterns

def printGraph(graph, msg):
    print("\nPrinting graph {}:".format(msg))
    print("The u's are:")
    for u in graph.u:
        print("    {}".format(u))
    ###print("The ui_to_idx's are:")
    ###for idx,ux in enumerate(graph.ui_to_idx):
    ###    print("    {} {}".format(idx, ux))
    print("The v's are:")
    for v in graph.v:
        print("    {}".format(v))
    ###print("The vj_to_idx's are:")
    ###for idx,vx in enumerate(graph.vj_to_idx):
    ###    print("    {} {}".format(idx, vx))
    print("The u_to_v's are:")
    for idx, u2v in enumerate(graph.u_to_v):
        print("    {} {}".format(idx, u2v))
    print("The v_to_u's are:")
    for idx, v2u in enumerate(graph.v_to_u):
        print("    {} {}".format(idx, v2u))

    print("\n")

def main():
    multiprocessing.set_start_method('spawn')

    parser = argparse.ArgumentParser()
    parser.add_argument('--database', required=True)
    parser.add_argument('--tile', required=True)
    parser.add_argument('--wire_to_node', action='store_true')
    parser.add_argument('--node_to_wires', action='store_true')
    parser.add_argument('--output_dir')
    parser.add_argument('--only_pips', action='store_true')

    args = parser.parse_args()

    if args.wire_to_node and args.node_to_wires:
        parser.error('Cannot supply both --wire_to_node and --node_to_wires')
    elif not args.wire_to_node and not args.node_to_wires:
        parser.error('Must supply --wire_to_node or --node_to_wires')

    if args.wire_to_node:
        print("#### Doing wire_to_node...")
        graph = get_wire_to_node_graph(args.database, args.tile)
    elif args.node_to_wires:
        #### print("#### Doing xxnode_to_wires...")
        graph = get_node_to_wires_graph(
            args.database, args.tile, args.only_pips)
        printGraph(graph, "Initial build")
    else:
        assert False

    print('\nProcessing {} : {}'.format(args.database, args.tile))

    #print(f"Done with first part at this point graph has these frozen edges:")
    #for edge in graph.frozen_edges:
    #    print(f"    Tile: {edge[0][0]}", end='')
    #    print(f" Node: {edge[1][0]}: ")
    #    for ntw in edge[1][1]:
    #        print(f"                           Wire: {ntw[0]}  {ntw[1]}, {ntw[2]}")

    #BEN
    if args.node_to_wires and args.only_pips:
        es = []
        for edge in graph.frozen_edges:
            ess = []
            for ntw in edge[1][1]:
                ess.append((ntw[0], ntw[1], ntw[2]))
            es.append((edge[0][0], edge[1][0], ess))
        es.sort()
        print(f"Tile, Node, Wire, dx, dy")
        for e in es:
            print(e)
        print("Tile, Node, Wire, dx, dy")

    if args.wire_to_node:
        print("There are {} frozen edges".format(len(graph.frozen_edges)))
        es = []
        for edge in graph.frozen_edges:
            es.append((edge[0].tile_pkey, edge[1].wire_in_tile_pkey, (edge[1].delta_x, edge[1].delta_y), edge[1].node_wire_in_tile_pkey))
        es.sort()
        print("Tile,  WITPK, dx, dx, NWITPK")
        for e in es:
            print(e)
        print("Tile,  WITPK, dx, dx, NWITPK")
            #print(f"Tile = {edge[0].tile_pkey} WireToNode: witpk= {edge[1].wire_in_tile_pkey} [{edge[1].delta_x}, {edge[1].delta_y}]  nwitpk= {edge[1].node_wire_in_tile_pkey}")
    


    all_edges = set(graph.frozen_edges)
    gc.collect()

    if len(all_edges) != 0:
        required_solutions, tile_patterns, tile_to_tile_patterns = reduce_graph(
            args, all_edges, graph)
    else:
        required_solutions = set()
        tile_patterns = set()
        tile_to_tile_patterns = {}

    if args.wire_to_node:
        write_wire_to_node(
            graph, required_solutions, tile_patterns, tile_to_tile_patterns,
            args.output_dir, args.tile)

    if args.node_to_wires:
        write_node_to_wires(
            graph, required_solutions, tile_patterns, tile_to_tile_patterns,
            args.output_dir, args.tile, args.only_pips)


if __name__ == "__main__":
    main()
