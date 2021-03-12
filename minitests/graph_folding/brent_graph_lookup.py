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

    print("\n")
    # Get handle to object of type NodeToWiresLookup
    ntwl = read_tile_type_n2w_pips_only(args.tile)

    for tile in ntwl.tile_to_tile_patterns:
        print(f"For tile: {tile}:")
        print(f"{len(ntwl.node_wire_in_tile_pkeys.items)}")
        for nwit in ntwl.node_wire_in_tile_pkeys.items:
            print(f"   {nwit}")
            for dx, dy, endnwit in ntwl.brent_get_wires_for_node(tile, nwit):
                print(f"   --> {endnwit} {dx}, {dy}")

if __name__ == "__main__":
    main()
