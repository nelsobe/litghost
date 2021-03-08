Processing build_xc7a100tfgg676-1/xc7a100tfgg676-1.db : CLK_PMV

% There are 3 nodes, each which terminate in a PIP at -1,-3 from the tile in question
Tile, Node, Wire, dx, dy
(9243, 8379, [(73944, -1, -3)])
(9243, 8435, [(73952, -1, -3)])
(9243, 8463, [(73956, -1, -3)])
Tile, Node, Wire, dx, dy
Node wires: 3
Max number of patterns: 1
Minimum number of pattern storage: 3
Unique wire in tile pkey 3
Unique node_to_wires 3
Unique patterns 3
Unique dx dy 1
Unique dx dy dist 3
density = 1.0, beta = 0.5, P = 48.938386452844064, N = 0.03
Found 1 possible complete subgraphs
There are 1 bicliques:
    s is one biclique and is a tuple (setOfTiles, setOfNodeToWire)
         Tiles:
               Tile(tile_pkey=9243)
         NodeToWires:
               (8379, frozenset({NodeToWire(wire_in_tile_pkey=73944, delta_x=-1, delta_y=-3)}))
               (8435, frozenset({NodeToWire(wire_in_tile_pkey=73952, delta_x=-1, delta_y=-3)}))
               (8463, frozenset({NodeToWire(wire_in_tile_pkey=73956, delta_x=-1, delta_y=-3)}))
1 complete subgraphs required for solution
| |                                           #                                                                      | 0 Elapsed Time: 0:00:04
Have 1 tile patterns
Max 1 patterns
Number of tile pattern elements: 1
Printing node_wire_tile_pkeys_array: len= 3
   0 8379
   1 8435
   2 8463
Wire patterns:  len= 3
   0 73944 -1, -3
   1 73952 -1, -3
   2 73956 -1, -3
Node_patterns_data:  len= 3
  0 (0,)
  1 (1,)
  2 (2,)
Subgraphs:  len= 1
  0: [0, 1, 2]
Tile_patterns_data:  len= 1
 0 (0,)
Tile_to_tile_patterns:  len= 2
  0 [9243]
  1 [0]
Size on disk:  384
##############################################################################
Access method:

subgraph = Tile_patterns_data[Tile_to_tile_patterns_hash(tileNum)]
