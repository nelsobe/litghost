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
import capnp
import capnp.lib.capnp
capnp.remove_import_hook()
import progressbar
import os.path

from node_lookup import NodeLookup

from graph_lookup import WireToNodeLookup, NodeToWiresLookup


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--database', required=True)
    parser.add_argument('--tile', required=True)
    parser.add_argument('--output_dir')

    args = parser.parse_args()

    graph_storage_schema = capnp.load('graph_storage.capnp')

    def read_tile_type_w2n(tile_type):
        return WireToNodeLookup(
            graph_storage_schema,
            os.path.join(
                args.output_dir, '{}_wire_to_nodes.bin'.format(tile_type)))

    def read_tile_type_n2w(tile_type):
        return NodeToWiresLookup(
            graph_storage_schema,
            os.path.join(
                args.output_dir, '{}_node_to_wires.bin'.format(tile_type)))

    def read_tile_type_n2w_pips_only(tile_type):
        return NodeToWiresLookup(
            graph_storage_schema,
            os.path.join(
                args.output_dir, '{}_node_to_pip_wires.bin'.format(tile_type)))

    lookup = NodeLookup(database=args.database)
    cur = lookup.conn.cursor()
    cur2 = lookup.conn.cursor()
    cur3 = lookup.conn.cursor()

    tile_xy_to_tile_pkey = {}
    tile_pkey_to_xy = {}
    tile_pkey_to_tile_type_name = {}
    tile_type_to_wire_to_node_lookup = {}
    tile_type_to_node_to_wires_lookup = {}
    tile_type_to_node_to_pip_wires_lookup = {}

    ########################################################################################
    #Collect all the tile info for this tile type and print it
    TileInfo = namedtuple('TileInfo', 'pkey ttype x y')
    tiles = {}
    for tile_pkey, tile_x, tile_y, tile_type_name in cur.execute("""
SELECT tile.pkey, tile.x, tile.y, tile_type.name
FROM tile
INNER JOIN tile_type ON tile.tile_type_pkey = tile_type.pkey;
    """):
        ti = TileInfo(tile_pkey, tile_type_name, tile_x, tile_y)
        if tile_type_name not in tiles:
            tiles[tile_type_name] = list()
        tiles[tile_type_name].append(ti)

    # tiles is a dict mapping tile type names (strings) to a list of physical tiles
    #   Each physical tile is represented by its pkey, type string, x, and y
    for key,val in tiles.items():
        if len(val) < 5:
            print(f"{key} {len(val)}")
            for item in val:
                print(f"{item.pkey}  {item.ttype}   {item.x}, {item.y}")

    # Get first tile of type requested
    ntwl = read_tile_type_n2w_pips_only(args.tile)
    tile,typ,x,y = tiles[args.tile][0]

    # For each node in this tile
    for node_pkey, wire_in_tile, name in cur2.execute("""
SELECT node.pkey, node.wire_in_tile_pkey, wire_in_tile.name
FROM node
INNER JOIN wire_in_tile ON node.wire_in_tile_pkey = wire_in_tile.pkey
WHERE node.tile_pkey = ?;
    """, (tile,)):
        #print("Doing node: {}".format(node_pkey))
        v = ntwl.get_wires_for_node(tile, x, y, wire_in_tile)
        if v is not None:
          for nx, ny, nwin in v:
            for name2 in cur3.execute("""
SELECT wire_in_tile.name 
FROM wire_in_tile
WHERE wire_in_tile.pkey = ?; 
            """, (nwin,)):
                print("Tile {}: {} has node {} whose wire is {} ({}) and who has other wire {} ({}) at [{}, {}]".format(args.tile, tile, node_pkey, wire_in_tile, name[0], nwin, name2[0], nx-x, ny-y))



if __name__ == "__main__":
    main()
