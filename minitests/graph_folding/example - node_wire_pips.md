 /usr/bin/env /home/nelson/prjxray/env/bin/python /home/nelson/.vscode-server/extensions/ms-python.python-2020.11.371526539/pythonFiles/lib/python/debugpy/launcher 35745 -- reduce_graph_for_type.py --database build_xc7a100tfgg676-1/xc7a100tfgg676-1.db --output_dir build_xc7a100tfgg676-1 --node_to_wires --only_pips --tile HCLK_CMT_L 
(env) nelson@CB461-EE11591:~/litghost/minitests/graph_folding$  /usr/bin/env /home/nelson/prjxray/env/bin/python /home/nelson/.vscode-server/extensions/ms-python.python-2020.11.371526539/pythonFiles/lib/python/debugpy/launcher 35745 -- reduce_graph_for_type.py --database build_xc7a100tfgg676-1/xc7a100tfgg676-1.db --output_dir build_xc7a100tfgg676-1 --node_to_wires --only_pips --tile HCLK_CMT_L 
source /home/nelson/prjxray/env/bin/activate
#### Doing node_to_wires...
Tile type pkey = 16, only_pips = True
/ |#                                                                                                                                                  | 0 Elapsed Time: 0:00:00  Got tile: 9710, 16, HCLK_CMT_L_X139Y78, 139/130
         Total nodes in tile = 60
  Got tile: 9711, 16, HCLK_CMT_L_X139Y130, 139/78
         Total nodes in tile = 60
| |#                                                                                                                                                  | 1 Elapsed Time: 0:00:00
      Total tiles = 2

Processing build_xc7a100tfgg676-1/xc7a100tfgg676-1.db : HCLK_CMT_L
Tile, Node, Wire, dx, dy
(9710, 9196, [(97685, 0, -5), (97689, 0, -57), (22362, 0, 8), (22366, 0, -44)])
(9710, 9197, [(97686, 0, -5), (22363, 0, 8), (97690, 0, -57), (22367, 0, -44)])
(9710, 9218, [(55219, -61, 0)])
(9710, 9219, [(55220, -61, 0)])
(9710, 9220, [(55221, -61, 0)])
(9710, 9221, [(55222, -61, 0)])
(9710, 9222, [(55223, -61, 0)])
(9710, 9223, [(55224, -61, 0)])
(9710, 9224, [(55225, -61, 0)])
(9710, 9225, [(55226, -61, 0)])
(9710, 9226, [(55227, -61, 0)])
(9710, 9227, [(55228, -61, 0)])
(9710, 9228, [(55229, -61, 0)])
(9710, 9229, [(55230, -61, 0)])
(9710, 9230, [(55231, -61, 0)])
(9710, 9231, [(55232, -61, 0)])
(9710, 9289, [(59556, 0, 17)])
(9710, 9290, [(59552, 0, 17)])
(9710, 9291, [(59554, 0, 17)])
(9710, 9300, [(11306, 7, 0)])
(9710, 9301, [(11307, 7, 0)])
(9710, 9302, [(11308, 7, 0)])
(9710, 9303, [(11309, 7, 0)])
(9710, 9304, [(33480, 0, -18)])
(9710, 9305, [(33481, 0, -18)])
(9710, 9306, [(33482, 0, -18)])
(9711, 9196, [(97685, 0, -5), (22364, 0, 60), (22362, 0, 8), (97687, 0, 47)])
(9711, 9197, [(97688, 0, 47), (97686, 0, -5), (22363, 0, 8), (22365, 0, 60)])
(9711, 9218, [(57359, -61, 0)])
(9711, 9219, [(57360, -61, 0)])
(9711, 9220, [(57361, -61, 0)])
(9711, 9221, [(57362, -61, 0)])
(9711, 9222, [(57363, -61, 0)])
(9711, 9223, [(57364, -61, 0)])
(9711, 9224, [(57365, -61, 0)])
(9711, 9225, [(57366, -61, 0)])
(9711, 9226, [(57367, -61, 0)])
(9711, 9227, [(57368, -61, 0)])
(9711, 9228, [(57369, -61, 0)])
(9711, 9229, [(57370, -61, 0)])
(9711, 9230, [(57371, -61, 0)])
(9711, 9231, [(57372, -61, 0)])
(9711, 9289, [(59556, 0, 17)])
(9711, 9290, [(59552, 0, 17)])
(9711, 9291, [(59554, 0, 17)])
(9711, 9300, [(11306, 7, 0)])
(9711, 9301, [(11307, 7, 0)])
(9711, 9302, [(11308, 7, 0)])
(9711, 9303, [(11309, 7, 0)])
(9711, 9304, [(33480, 0, -18)])
(9711, 9305, [(33481, 0, -18)])
(9711, 9306, [(33482, 0, -18)])
Tile, Node, Wire, dx, dy
Node wires: 26
Max number of patterns: 4
Minimum number of pattern storage: 54
Unique wire in tile pkey 50
Unique node_to_wires 42
Unique patterns 50
Unique dx dy 10
Unique dx dy dist 61
density = 0.6190476190476191, beta = 0.5, P = 6.021425301403878, N = 0.84
Found 3 possible complete subgraphs
2 complete subgraphs required for solution
| |                                           #                                                                                                       | 1 Elapsed Time: 0:00:04
Have 2 tile patterns
Max 1 patterns
Number of tile pattern elements: 2
Tile to tile patterns: <reference_model.StructOfArray object at 0x7f2120170400>
Printing node_wire_tile_pkeys_array:
  0 9196 
  1 9197 
  2 9218 
  3 9219 
  4 9220 
  5 9221 
  6 9222 
  7 9223 
  8 9224 
  9 9225 
  10 9226 
  11 9227 
  12 9228 
  13 9229 
  14 9230 
  15 9231 
  16 9289 
  17 9290 
  18 9291 
  19 9300 
  20 9301 
  21 9302 
  22 9303 
  23 9304 
  24 9305 
  25 9306 
Wire patterns: 
  55219 -61, 0
  55220 -61, 0
  55221 -61, 0
  55222 -61, 0
  55223 -61, 0
  55224 -61, 0
  55225 -61, 0
  55226 -61, 0
  55227 -61, 0
  55228 -61, 0
  55229 -61, 0
  55230 -61, 0
  55231 -61, 0
  55232 -61, 0
  57359 -61, 0
  57360 -61, 0
  57361 -61, 0
  57362 -61, 0
  57363 -61, 0
  57364 -61, 0
  57365 -61, 0
  57366 -61, 0
  57367 -61, 0
  57368 -61, 0
  57369 -61, 0
  57370 -61, 0
  57371 -61, 0
  57372 -61, 0
  97689 0, -57
  97690 0, -57
  22366 0, -44
  22367 0, -44
  33480 0, -18
  33481 0, -18
  33482 0, -18
  97685 0, -5
  97686 0, -5
  22362 0, 8
  22363 0, 8
  59552 0, 17
  59554 0, 17
  59556 0, 17
  97687 0, 47
  97688 0, 47
  22364 0, 60
  22365 0, 60
  11306 7, 0
  11307 7, 0
  11308 7, 0
  11309 7, 0
Node_patterns_data:
  0 (32,)
  1 (47,)
  2 (21,)
  3 (27,)
  4 (16,)
  5 (14,)
  6 (48,)
  7 (35, 37, 42, 44)
  8 (15,)
  9 (41,)
  10 (40,)
  11 (20,)
  12 (39,)
  13 (46,)
  14 (25,)
  15 (34,)
  16 (36, 38, 43, 45)
  17 (23,)
  18 (17,)
  19 (24,)
  20 (26,)
  21 (33,)
  22 (18,)
  23 (22,)
  24 (19,)
  25 (49,)
  26 (12,)
  27 (7,)
  28 (11,)
  29 (3,)
  30 (8,)
  31 (28, 30, 35, 37)
  32 (9,)
  33 (10,)
  34 (4,)
  35 (1,)
  36 (2,)
  37 (13,)
  38 (29, 31, 36, 38)
  39 (0,)
  40 (5,)
  41 (6,)
Subgraphs:
  [7, 16, 5, 8, 4, 18, 22, 24, 11, 2, 23, 17, 19, 14, 20, 3, 9, 12, 10, 13, 1, 6, 25, 0, 21, 15]
  [31, 38, 39, 35, 36, 29, 34, 40, 41, 27, 30, 32, 33, 28, 26, 37, 9, 12, 10, 13, 1, 6, 25, 0, 21, 15]
Tile_patterns_data:
  (1,)
  (0,)
Tile_to_tile_patterns:
  [9710, 9711]
  [0, 1]
Size on disk:  1840

To do a lookup:

1. Find tile you want in Tile_to_tile patterns
2. Use its index to index into Tile_patterns_data
3. Use the value found to select a subgraph.  
    - You now have the right subgraph
4. Find node in node_wire_tile_pkeys_array
5. Use its position as index into subgraph from #3
6. Entry in node patterns at that locatiuon gives node_wire_in_tile_pkey, dx, and dy.
    - So you have full tuple: tile from #1, wire_in_tile_pkey from #4, node_wire_in_tile_pkey, dx, and dy from #6
    