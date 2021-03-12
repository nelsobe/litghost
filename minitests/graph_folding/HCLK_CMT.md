(litghost) nelson@ubuntu:~/litghost/minitests/graph_folding$ make one_pattern 
python3 brent_reduce_graph_for_type.py \
                        --database build_xc7a100tfgg676-1/xc7a100tfgg676-1.db \
                        --output_dir build_xc7a100tfgg676-1 \
                        --node_to_wires \
                        --only_pips \
                        --tile HCLK_CMT
Tile type pkey = 106, only_pips = True
/ |#                                                                                                                | 0 Elapsed Time: 0:00:00  Looking at tile: 9712, 106, HCLK_CMT_X8Y26, 8/182
  Looking at tile: 9713, 106, HCLK_CMT_X8Y78, 8/130
  Looking at tile: 9714, 106, HCLK_CMT_X8Y130, 8/78
  Looking at tile: 9715, 106, HCLK_CMT_X8Y182, 8/26
| |#                                                                                                                | 3 Elapsed Time: 0:00:00
      Total tiles = 4

Printing graph Initial build:
The u's are:
    Tile(tile_pkey=9712)
    Tile(tile_pkey=9713)
    Tile(tile_pkey=9714)
    Tile(tile_pkey=9715)
The v's are:
    (84936, frozenset({NodeToWire(wire_in_tile_pkey=18958, delta_x=0, delta_y=-57), NodeToWire(wire_in_tile_pkey=3059, delta_x=0, delta_y=-44), NodeToWire(wire_in_tile_pkey=3055, delta_x=0, delta_y=8), NodeToWire(wire_in_tile_pkey=18954, delta_x=0, delta_y=-5)}))
    (84936, frozenset({NodeToWire(wire_in_tile_pkey=3055, delta_x=0, delta_y=8), NodeToWire(wire_in_tile_pkey=18956, delta_x=0, delta_y=47), NodeToWire(wire_in_tile_pkey=18954, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=3057, delta_x=0, delta_y=60)}))
    (84936, frozenset({NodeToWire(wire_in_tile_pkey=18958, delta_x=0, delta_y=-57), NodeToWire(wire_in_tile_pkey=3059, delta_x=0, delta_y=-44), NodeToWire(wire_in_tile_pkey=18956, delta_x=0, delta_y=47), NodeToWire(wire_in_tile_pkey=18954, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=3057, delta_x=0, delta_y=60), NodeToWire(wire_in_tile_pkey=3055, delta_x=0, delta_y=8)}))
    (84937, frozenset({NodeToWire(wire_in_tile_pkey=3060, delta_x=0, delta_y=-44), NodeToWire(wire_in_tile_pkey=18955, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=18959, delta_x=0, delta_y=-57), NodeToWire(wire_in_tile_pkey=3056, delta_x=0, delta_y=8)}))
    (84937, frozenset({NodeToWire(wire_in_tile_pkey=18957, delta_x=0, delta_y=47), NodeToWire(wire_in_tile_pkey=18955, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=3058, delta_x=0, delta_y=60), NodeToWire(wire_in_tile_pkey=3056, delta_x=0, delta_y=8)}))
    (84937, frozenset({NodeToWire(wire_in_tile_pkey=3056, delta_x=0, delta_y=8), NodeToWire(wire_in_tile_pkey=18955, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=3060, delta_x=0, delta_y=-44), NodeToWire(wire_in_tile_pkey=18957, delta_x=0, delta_y=47), NodeToWire(wire_in_tile_pkey=3058, delta_x=0, delta_y=60), NodeToWire(wire_in_tile_pkey=18959, delta_x=0, delta_y=-57)}))
    (84989, frozenset({NodeToWire(wire_in_tile_pkey=57341, delta_x=70, delta_y=0)}))
    (84989, frozenset({NodeToWire(wire_in_tile_pkey=55201, delta_x=70, delta_y=0)}))
    (84990, frozenset({NodeToWire(wire_in_tile_pkey=55202, delta_x=70, delta_y=0)}))
    (84990, frozenset({NodeToWire(wire_in_tile_pkey=57342, delta_x=70, delta_y=0)}))
    (84991, frozenset({NodeToWire(wire_in_tile_pkey=57343, delta_x=70, delta_y=0)}))
    (84991, frozenset({NodeToWire(wire_in_tile_pkey=55203, delta_x=70, delta_y=0)}))
    (84992, frozenset({NodeToWire(wire_in_tile_pkey=57344, delta_x=70, delta_y=0)}))
    (84992, frozenset({NodeToWire(wire_in_tile_pkey=55204, delta_x=70, delta_y=0)}))
    (84993, frozenset({NodeToWire(wire_in_tile_pkey=57345, delta_x=70, delta_y=0)}))
    (84993, frozenset({NodeToWire(wire_in_tile_pkey=55205, delta_x=70, delta_y=0)}))
    (84994, frozenset({NodeToWire(wire_in_tile_pkey=57346, delta_x=70, delta_y=0)}))
    (84994, frozenset({NodeToWire(wire_in_tile_pkey=55206, delta_x=70, delta_y=0)}))
    (84995, frozenset({NodeToWire(wire_in_tile_pkey=55207, delta_x=70, delta_y=0)}))
    (84995, frozenset({NodeToWire(wire_in_tile_pkey=57347, delta_x=70, delta_y=0)}))
    (84996, frozenset({NodeToWire(wire_in_tile_pkey=57348, delta_x=70, delta_y=0)}))
    (84996, frozenset({NodeToWire(wire_in_tile_pkey=55208, delta_x=70, delta_y=0)}))
    (84997, frozenset({NodeToWire(wire_in_tile_pkey=57349, delta_x=70, delta_y=0)}))
    (84997, frozenset({NodeToWire(wire_in_tile_pkey=55209, delta_x=70, delta_y=0)}))
    (84998, frozenset({NodeToWire(wire_in_tile_pkey=55210, delta_x=70, delta_y=0)}))
    (84998, frozenset({NodeToWire(wire_in_tile_pkey=57350, delta_x=70, delta_y=0)}))
    (84999, frozenset({NodeToWire(wire_in_tile_pkey=55211, delta_x=70, delta_y=0)}))
    (84999, frozenset({NodeToWire(wire_in_tile_pkey=57351, delta_x=70, delta_y=0)}))
    (85000, frozenset({NodeToWire(wire_in_tile_pkey=57352, delta_x=70, delta_y=0)}))
    (85000, frozenset({NodeToWire(wire_in_tile_pkey=55212, delta_x=70, delta_y=0)}))
    (85001, frozenset({NodeToWire(wire_in_tile_pkey=57353, delta_x=70, delta_y=0)}))
    (85001, frozenset({NodeToWire(wire_in_tile_pkey=55213, delta_x=70, delta_y=0)}))
    (85002, frozenset({NodeToWire(wire_in_tile_pkey=57354, delta_x=70, delta_y=0)}))
    (85002, frozenset({NodeToWire(wire_in_tile_pkey=55214, delta_x=70, delta_y=0)}))
    (85029, frozenset({NodeToWire(wire_in_tile_pkey=45985, delta_x=0, delta_y=17)}))
    (85030, frozenset({NodeToWire(wire_in_tile_pkey=45981, delta_x=0, delta_y=17)}))
    (85031, frozenset({NodeToWire(wire_in_tile_pkey=45983, delta_x=0, delta_y=17)}))
    (85040, frozenset({NodeToWire(wire_in_tile_pkey=11306, delta_x=-7, delta_y=0)}))
    (85041, frozenset({NodeToWire(wire_in_tile_pkey=11307, delta_x=-7, delta_y=0)}))
    (85042, frozenset({NodeToWire(wire_in_tile_pkey=11308, delta_x=-7, delta_y=0)}))
    (85043, frozenset({NodeToWire(wire_in_tile_pkey=11309, delta_x=-7, delta_y=0)}))
    (85044, frozenset({NodeToWire(wire_in_tile_pkey=43566, delta_x=0, delta_y=-18)}))
    (85045, frozenset({NodeToWire(wire_in_tile_pkey=43567, delta_x=0, delta_y=-18)}))
    (85046, frozenset({NodeToWire(wire_in_tile_pkey=43568, delta_x=0, delta_y=-18)}))
The u_to_v's are:
    0 bitarray('10010001100101010110010110100101011111111111')
    1 bitarray('00100101100101010110010110100101011111111111')
    2 bitarray('00100110011010101001101001011010101111111111')
    3 bitarray('01001010011010101001101001011010101111111111')
The v_to_u's are:
    0 bitarray('1000')
    1 bitarray('0001')
    2 bitarray('0110')
    3 bitarray('1000')
    4 bitarray('0001')
    5 bitarray('0110')
    6 bitarray('0011')
    7 bitarray('1100')
    8 bitarray('1100')
    9 bitarray('0011')
    10 bitarray('0011')
    11 bitarray('1100')
    12 bitarray('0011')
    13 bitarray('1100')
    14 bitarray('0011')
    15 bitarray('1100')
    16 bitarray('0011')
    17 bitarray('1100')
    18 bitarray('1100')
    19 bitarray('0011')
    20 bitarray('0011')
    21 bitarray('1100')
    22 bitarray('0011')
    23 bitarray('1100')
    24 bitarray('1100')
    25 bitarray('0011')
    26 bitarray('1100')
    27 bitarray('0011')
    28 bitarray('0011')
    29 bitarray('1100')
    30 bitarray('0011')
    31 bitarray('1100')
    32 bitarray('0011')
    33 bitarray('1100')
    34 bitarray('1111')
    35 bitarray('1111')
    36 bitarray('1111')
    37 bitarray('1111')
    38 bitarray('1111')
    39 bitarray('1111')
    40 bitarray('1111')
    41 bitarray('1111')
    42 bitarray('1111')
    43 bitarray('1111')



Processing build_xc7a100tfgg676-1/xc7a100tfgg676-1.db : HCLK_CMT
Tile, Node_wire_in_tile, Wire, dx, dy
(9712, 84936, [(18958, 0, -57), (3059, 0, -44), (3055, 0, 8), (18954, 0, -5)])
(9712, 84937, [(3060, 0, -44), (18955, 0, -5), (18959, 0, -57), (3056, 0, 8)])
(9712, 84989, [(55201, 70, 0)])
(9712, 84990, [(55202, 70, 0)])
(9712, 84991, [(55203, 70, 0)])
(9712, 84992, [(55204, 70, 0)])
(9712, 84993, [(55205, 70, 0)])
(9712, 84994, [(55206, 70, 0)])
(9712, 84995, [(55207, 70, 0)])
(9712, 84996, [(55208, 70, 0)])
(9712, 84997, [(55209, 70, 0)])
(9712, 84998, [(55210, 70, 0)])
(9712, 84999, [(55211, 70, 0)])
(9712, 85000, [(55212, 70, 0)])
(9712, 85001, [(55213, 70, 0)])
(9712, 85002, [(55214, 70, 0)])
(9712, 85029, [(45985, 0, 17)])
(9712, 85030, [(45981, 0, 17)])
(9712, 85031, [(45983, 0, 17)])
(9712, 85040, [(11306, -7, 0)])
(9712, 85041, [(11307, -7, 0)])
(9712, 85042, [(11308, -7, 0)])
(9712, 85043, [(11309, -7, 0)])
(9712, 85044, [(43566, 0, -18)])
(9712, 85045, [(43567, 0, -18)])
(9712, 85046, [(43568, 0, -18)])
(9713, 84936, [(18958, 0, -57), (3059, 0, -44), (18956, 0, 47), (18954, 0, -5), (3057, 0, 60), (3055, 0, 8)])
(9713, 84937, [(3056, 0, 8), (18955, 0, -5), (3060, 0, -44), (18957, 0, 47), (3058, 0, 60), (18959, 0, -57)])
(9713, 84989, [(55201, 70, 0)])
(9713, 84990, [(55202, 70, 0)])
(9713, 84991, [(55203, 70, 0)])
(9713, 84992, [(55204, 70, 0)])
(9713, 84993, [(55205, 70, 0)])
(9713, 84994, [(55206, 70, 0)])
(9713, 84995, [(55207, 70, 0)])
(9713, 84996, [(55208, 70, 0)])
(9713, 84997, [(55209, 70, 0)])
(9713, 84998, [(55210, 70, 0)])
(9713, 84999, [(55211, 70, 0)])
(9713, 85000, [(55212, 70, 0)])
(9713, 85001, [(55213, 70, 0)])
(9713, 85002, [(55214, 70, 0)])
(9713, 85029, [(45985, 0, 17)])
(9713, 85030, [(45981, 0, 17)])
(9713, 85031, [(45983, 0, 17)])
(9713, 85040, [(11306, -7, 0)])
(9713, 85041, [(11307, -7, 0)])
(9713, 85042, [(11308, -7, 0)])
(9713, 85043, [(11309, -7, 0)])
(9713, 85044, [(43566, 0, -18)])
(9713, 85045, [(43567, 0, -18)])
(9713, 85046, [(43568, 0, -18)])
(9714, 84936, [(18958, 0, -57), (3059, 0, -44), (18956, 0, 47), (18954, 0, -5), (3057, 0, 60), (3055, 0, 8)])
(9714, 84937, [(3056, 0, 8), (18955, 0, -5), (3060, 0, -44), (18957, 0, 47), (3058, 0, 60), (18959, 0, -57)])
(9714, 84989, [(57341, 70, 0)])
(9714, 84990, [(57342, 70, 0)])
(9714, 84991, [(57343, 70, 0)])
(9714, 84992, [(57344, 70, 0)])
(9714, 84993, [(57345, 70, 0)])
(9714, 84994, [(57346, 70, 0)])
(9714, 84995, [(57347, 70, 0)])
(9714, 84996, [(57348, 70, 0)])
(9714, 84997, [(57349, 70, 0)])
(9714, 84998, [(57350, 70, 0)])
(9714, 84999, [(57351, 70, 0)])
(9714, 85000, [(57352, 70, 0)])
(9714, 85001, [(57353, 70, 0)])
(9714, 85002, [(57354, 70, 0)])
(9714, 85029, [(45985, 0, 17)])
(9714, 85030, [(45981, 0, 17)])
(9714, 85031, [(45983, 0, 17)])
(9714, 85040, [(11306, -7, 0)])
(9714, 85041, [(11307, -7, 0)])
(9714, 85042, [(11308, -7, 0)])
(9714, 85043, [(11309, -7, 0)])
(9714, 85044, [(43566, 0, -18)])
(9714, 85045, [(43567, 0, -18)])
(9714, 85046, [(43568, 0, -18)])
(9715, 84936, [(3055, 0, 8), (18956, 0, 47), (18954, 0, -5), (3057, 0, 60)])
(9715, 84937, [(18957, 0, 47), (18955, 0, -5), (3058, 0, 60), (3056, 0, 8)])
(9715, 84989, [(57341, 70, 0)])
(9715, 84990, [(57342, 70, 0)])
(9715, 84991, [(57343, 70, 0)])
(9715, 84992, [(57344, 70, 0)])
(9715, 84993, [(57345, 70, 0)])
(9715, 84994, [(57346, 70, 0)])
(9715, 84995, [(57347, 70, 0)])
(9715, 84996, [(57348, 70, 0)])
(9715, 84997, [(57349, 70, 0)])
(9715, 84998, [(57350, 70, 0)])
(9715, 84999, [(57351, 70, 0)])
(9715, 85000, [(57352, 70, 0)])
(9715, 85001, [(57353, 70, 0)])
(9715, 85002, [(57354, 70, 0)])
(9715, 85029, [(45985, 0, 17)])
(9715, 85030, [(45981, 0, 17)])
(9715, 85031, [(45983, 0, 17)])
(9715, 85040, [(11306, -7, 0)])
(9715, 85041, [(11307, -7, 0)])
(9715, 85042, [(11308, -7, 0)])
(9715, 85043, [(11309, -7, 0)])
(9715, 85044, [(43566, 0, -18)])
(9715, 85045, [(43567, 0, -18)])
(9715, 85046, [(43568, 0, -18)])
Tile, Node_wire_in_tile, Wire, dx, dy
Node wires: 26
Max number of patterns: 6
Minimum number of pattern storage: 66
Unique wire in tile pkey 50
Unique node_to_wires 44
Unique patterns 50
Unique dx dy 10
Unique dx dy dist 70
density = 0.5909090909090909, beta = 0.5, P = 5.158067983438611, N = 1.76
Found 8 possible complete subgraphs
There are 8 bicliques:
    s is one biclique and is a tuple (setOfTiles, setOfNodeToWire)
         Tiles:
               Tile(tile_pkey=9715)
               Tile(tile_pkey=9714)
         NodeToWires:
               (85046, frozenset({NodeToWire(wire_in_tile_pkey=43568, delta_x=0, delta_y=-18)}))
               (85040, frozenset({NodeToWire(wire_in_tile_pkey=11306, delta_x=-7, delta_y=0)}))
               (85042, frozenset({NodeToWire(wire_in_tile_pkey=11308, delta_x=-7, delta_y=0)}))
               (84997, frozenset({NodeToWire(wire_in_tile_pkey=57349, delta_x=70, delta_y=0)}))
               (85001, frozenset({NodeToWire(wire_in_tile_pkey=57353, delta_x=70, delta_y=0)}))
               (84991, frozenset({NodeToWire(wire_in_tile_pkey=57343, delta_x=70, delta_y=0)}))
               (85045, frozenset({NodeToWire(wire_in_tile_pkey=43567, delta_x=0, delta_y=-18)}))
               (85043, frozenset({NodeToWire(wire_in_tile_pkey=11309, delta_x=-7, delta_y=0)}))
               (84992, frozenset({NodeToWire(wire_in_tile_pkey=57344, delta_x=70, delta_y=0)}))
               (84994, frozenset({NodeToWire(wire_in_tile_pkey=57346, delta_x=70, delta_y=0)}))
               (85029, frozenset({NodeToWire(wire_in_tile_pkey=45985, delta_x=0, delta_y=17)}))
               (84996, frozenset({NodeToWire(wire_in_tile_pkey=57348, delta_x=70, delta_y=0)}))
               (85031, frozenset({NodeToWire(wire_in_tile_pkey=45983, delta_x=0, delta_y=17)}))
               (84990, frozenset({NodeToWire(wire_in_tile_pkey=57342, delta_x=70, delta_y=0)}))
               (85030, frozenset({NodeToWire(wire_in_tile_pkey=45981, delta_x=0, delta_y=17)}))
               (85000, frozenset({NodeToWire(wire_in_tile_pkey=57352, delta_x=70, delta_y=0)}))
               (84995, frozenset({NodeToWire(wire_in_tile_pkey=57347, delta_x=70, delta_y=0)}))
               (84999, frozenset({NodeToWire(wire_in_tile_pkey=57351, delta_x=70, delta_y=0)}))
               (84989, frozenset({NodeToWire(wire_in_tile_pkey=57341, delta_x=70, delta_y=0)}))
               (85044, frozenset({NodeToWire(wire_in_tile_pkey=43566, delta_x=0, delta_y=-18)}))
               (85002, frozenset({NodeToWire(wire_in_tile_pkey=57354, delta_x=70, delta_y=0)}))
               (84993, frozenset({NodeToWire(wire_in_tile_pkey=57345, delta_x=70, delta_y=0)}))
               (85041, frozenset({NodeToWire(wire_in_tile_pkey=11307, delta_x=-7, delta_y=0)}))
               (84998, frozenset({NodeToWire(wire_in_tile_pkey=57350, delta_x=70, delta_y=0)}))
    s is one biclique and is a tuple (setOfTiles, setOfNodeToWire)
         Tiles:
               Tile(tile_pkey=9712)
         NodeToWires:
               (85046, frozenset({NodeToWire(wire_in_tile_pkey=43568, delta_x=0, delta_y=-18)}))
               (85040, frozenset({NodeToWire(wire_in_tile_pkey=11306, delta_x=-7, delta_y=0)}))
               (84937, frozenset({NodeToWire(wire_in_tile_pkey=3060, delta_x=0, delta_y=-44), NodeToWire(wire_in_tile_pkey=18955, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=18959, delta_x=0, delta_y=-57), NodeToWire(wire_in_tile_pkey=3056, delta_x=0, delta_y=8)}))
               (85042, frozenset({NodeToWire(wire_in_tile_pkey=11308, delta_x=-7, delta_y=0)}))
               (84990, frozenset({NodeToWire(wire_in_tile_pkey=55202, delta_x=70, delta_y=0)}))
               (84995, frozenset({NodeToWire(wire_in_tile_pkey=55207, delta_x=70, delta_y=0)}))
               (84936, frozenset({NodeToWire(wire_in_tile_pkey=18958, delta_x=0, delta_y=-57), NodeToWire(wire_in_tile_pkey=3059, delta_x=0, delta_y=-44), NodeToWire(wire_in_tile_pkey=3055, delta_x=0, delta_y=8), NodeToWire(wire_in_tile_pkey=18954, delta_x=0, delta_y=-5)}))
               (84998, frozenset({NodeToWire(wire_in_tile_pkey=55210, delta_x=70, delta_y=0)}))
               (85045, frozenset({NodeToWire(wire_in_tile_pkey=43567, delta_x=0, delta_y=-18)}))
               (85043, frozenset({NodeToWire(wire_in_tile_pkey=11309, delta_x=-7, delta_y=0)}))
               (85029, frozenset({NodeToWire(wire_in_tile_pkey=45985, delta_x=0, delta_y=17)}))
               (84992, frozenset({NodeToWire(wire_in_tile_pkey=55204, delta_x=70, delta_y=0)}))
               (85031, frozenset({NodeToWire(wire_in_tile_pkey=45983, delta_x=0, delta_y=17)}))
               (84996, frozenset({NodeToWire(wire_in_tile_pkey=55208, delta_x=70, delta_y=0)}))
               (84997, frozenset({NodeToWire(wire_in_tile_pkey=55209, delta_x=70, delta_y=0)}))
               (85030, frozenset({NodeToWire(wire_in_tile_pkey=45981, delta_x=0, delta_y=17)}))
               (84999, frozenset({NodeToWire(wire_in_tile_pkey=55211, delta_x=70, delta_y=0)}))
               (85044, frozenset({NodeToWire(wire_in_tile_pkey=43566, delta_x=0, delta_y=-18)}))
               (84991, frozenset({NodeToWire(wire_in_tile_pkey=55203, delta_x=70, delta_y=0)}))
               (84989, frozenset({NodeToWire(wire_in_tile_pkey=55201, delta_x=70, delta_y=0)}))
               (85041, frozenset({NodeToWire(wire_in_tile_pkey=11307, delta_x=-7, delta_y=0)}))
               (84994, frozenset({NodeToWire(wire_in_tile_pkey=55206, delta_x=70, delta_y=0)}))
               (85001, frozenset({NodeToWire(wire_in_tile_pkey=55213, delta_x=70, delta_y=0)}))
               (85002, frozenset({NodeToWire(wire_in_tile_pkey=55214, delta_x=70, delta_y=0)}))
               (85000, frozenset({NodeToWire(wire_in_tile_pkey=55212, delta_x=70, delta_y=0)}))
               (84993, frozenset({NodeToWire(wire_in_tile_pkey=55205, delta_x=70, delta_y=0)}))
    s is one biclique and is a tuple (setOfTiles, setOfNodeToWire)
         Tiles:
               Tile(tile_pkey=9712)
               Tile(tile_pkey=9713)
         NodeToWires:
               (85046, frozenset({NodeToWire(wire_in_tile_pkey=43568, delta_x=0, delta_y=-18)}))
               (85040, frozenset({NodeToWire(wire_in_tile_pkey=11306, delta_x=-7, delta_y=0)}))
               (85042, frozenset({NodeToWire(wire_in_tile_pkey=11308, delta_x=-7, delta_y=0)}))
               (84990, frozenset({NodeToWire(wire_in_tile_pkey=55202, delta_x=70, delta_y=0)}))
               (84995, frozenset({NodeToWire(wire_in_tile_pkey=55207, delta_x=70, delta_y=0)}))
               (84998, frozenset({NodeToWire(wire_in_tile_pkey=55210, delta_x=70, delta_y=0)}))
               (85045, frozenset({NodeToWire(wire_in_tile_pkey=43567, delta_x=0, delta_y=-18)}))
               (85043, frozenset({NodeToWire(wire_in_tile_pkey=11309, delta_x=-7, delta_y=0)}))
               (85029, frozenset({NodeToWire(wire_in_tile_pkey=45985, delta_x=0, delta_y=17)}))
               (84992, frozenset({NodeToWire(wire_in_tile_pkey=55204, delta_x=70, delta_y=0)}))
               (85031, frozenset({NodeToWire(wire_in_tile_pkey=45983, delta_x=0, delta_y=17)}))
               (84996, frozenset({NodeToWire(wire_in_tile_pkey=55208, delta_x=70, delta_y=0)}))
               (84997, frozenset({NodeToWire(wire_in_tile_pkey=55209, delta_x=70, delta_y=0)}))
               (85030, frozenset({NodeToWire(wire_in_tile_pkey=45981, delta_x=0, delta_y=17)}))
               (84999, frozenset({NodeToWire(wire_in_tile_pkey=55211, delta_x=70, delta_y=0)}))
               (85044, frozenset({NodeToWire(wire_in_tile_pkey=43566, delta_x=0, delta_y=-18)}))
               (84991, frozenset({NodeToWire(wire_in_tile_pkey=55203, delta_x=70, delta_y=0)}))
               (84989, frozenset({NodeToWire(wire_in_tile_pkey=55201, delta_x=70, delta_y=0)}))
               (85041, frozenset({NodeToWire(wire_in_tile_pkey=11307, delta_x=-7, delta_y=0)}))
               (84994, frozenset({NodeToWire(wire_in_tile_pkey=55206, delta_x=70, delta_y=0)}))
               (85001, frozenset({NodeToWire(wire_in_tile_pkey=55213, delta_x=70, delta_y=0)}))
               (85002, frozenset({NodeToWire(wire_in_tile_pkey=55214, delta_x=70, delta_y=0)}))
               (85000, frozenset({NodeToWire(wire_in_tile_pkey=55212, delta_x=70, delta_y=0)}))
               (84993, frozenset({NodeToWire(wire_in_tile_pkey=55205, delta_x=70, delta_y=0)}))
    s is one biclique and is a tuple (setOfTiles, setOfNodeToWire)
         Tiles:
               Tile(tile_pkey=9713)
         NodeToWires:
               (85046, frozenset({NodeToWire(wire_in_tile_pkey=43568, delta_x=0, delta_y=-18)}))
               (85040, frozenset({NodeToWire(wire_in_tile_pkey=11306, delta_x=-7, delta_y=0)}))
               (85042, frozenset({NodeToWire(wire_in_tile_pkey=11308, delta_x=-7, delta_y=0)}))
               (84936, frozenset({NodeToWire(wire_in_tile_pkey=18958, delta_x=0, delta_y=-57), NodeToWire(wire_in_tile_pkey=3059, delta_x=0, delta_y=-44), NodeToWire(wire_in_tile_pkey=18956, delta_x=0, delta_y=47), NodeToWire(wire_in_tile_pkey=18954, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=3057, delta_x=0, delta_y=60), NodeToWire(wire_in_tile_pkey=3055, delta_x=0, delta_y=8)}))
               (84990, frozenset({NodeToWire(wire_in_tile_pkey=55202, delta_x=70, delta_y=0)}))
               (84995, frozenset({NodeToWire(wire_in_tile_pkey=55207, delta_x=70, delta_y=0)}))
               (84998, frozenset({NodeToWire(wire_in_tile_pkey=55210, delta_x=70, delta_y=0)}))
               (85045, frozenset({NodeToWire(wire_in_tile_pkey=43567, delta_x=0, delta_y=-18)}))
               (85043, frozenset({NodeToWire(wire_in_tile_pkey=11309, delta_x=-7, delta_y=0)}))
               (85029, frozenset({NodeToWire(wire_in_tile_pkey=45985, delta_x=0, delta_y=17)}))
               (84992, frozenset({NodeToWire(wire_in_tile_pkey=55204, delta_x=70, delta_y=0)}))
               (85031, frozenset({NodeToWire(wire_in_tile_pkey=45983, delta_x=0, delta_y=17)}))
               (84996, frozenset({NodeToWire(wire_in_tile_pkey=55208, delta_x=70, delta_y=0)}))
               (84997, frozenset({NodeToWire(wire_in_tile_pkey=55209, delta_x=70, delta_y=0)}))
               (85030, frozenset({NodeToWire(wire_in_tile_pkey=45981, delta_x=0, delta_y=17)}))
               (84999, frozenset({NodeToWire(wire_in_tile_pkey=55211, delta_x=70, delta_y=0)}))
               (84937, frozenset({NodeToWire(wire_in_tile_pkey=3056, delta_x=0, delta_y=8), NodeToWire(wire_in_tile_pkey=18955, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=3060, delta_x=0, delta_y=-44), NodeToWire(wire_in_tile_pkey=18957, delta_x=0, delta_y=47), NodeToWire(wire_in_tile_pkey=3058, delta_x=0, delta_y=60), NodeToWire(wire_in_tile_pkey=18959, delta_x=0, delta_y=-57)}))
               (85044, frozenset({NodeToWire(wire_in_tile_pkey=43566, delta_x=0, delta_y=-18)}))
               (84991, frozenset({NodeToWire(wire_in_tile_pkey=55203, delta_x=70, delta_y=0)}))
               (84989, frozenset({NodeToWire(wire_in_tile_pkey=55201, delta_x=70, delta_y=0)}))
               (85041, frozenset({NodeToWire(wire_in_tile_pkey=11307, delta_x=-7, delta_y=0)}))
               (84994, frozenset({NodeToWire(wire_in_tile_pkey=55206, delta_x=70, delta_y=0)}))
               (85001, frozenset({NodeToWire(wire_in_tile_pkey=55213, delta_x=70, delta_y=0)}))
               (85002, frozenset({NodeToWire(wire_in_tile_pkey=55214, delta_x=70, delta_y=0)}))
               (85000, frozenset({NodeToWire(wire_in_tile_pkey=55212, delta_x=70, delta_y=0)}))
               (84993, frozenset({NodeToWire(wire_in_tile_pkey=55205, delta_x=70, delta_y=0)}))
    s is one biclique and is a tuple (setOfTiles, setOfNodeToWire)
         Tiles:
               Tile(tile_pkey=9715)
         NodeToWires:
               (85046, frozenset({NodeToWire(wire_in_tile_pkey=43568, delta_x=0, delta_y=-18)}))
               (85040, frozenset({NodeToWire(wire_in_tile_pkey=11306, delta_x=-7, delta_y=0)}))
               (85042, frozenset({NodeToWire(wire_in_tile_pkey=11308, delta_x=-7, delta_y=0)}))
               (84997, frozenset({NodeToWire(wire_in_tile_pkey=57349, delta_x=70, delta_y=0)}))
               (85001, frozenset({NodeToWire(wire_in_tile_pkey=57353, delta_x=70, delta_y=0)}))
               (84991, frozenset({NodeToWire(wire_in_tile_pkey=57343, delta_x=70, delta_y=0)}))
               (85045, frozenset({NodeToWire(wire_in_tile_pkey=43567, delta_x=0, delta_y=-18)}))
               (85043, frozenset({NodeToWire(wire_in_tile_pkey=11309, delta_x=-7, delta_y=0)}))
               (84992, frozenset({NodeToWire(wire_in_tile_pkey=57344, delta_x=70, delta_y=0)}))
               (84936, frozenset({NodeToWire(wire_in_tile_pkey=3055, delta_x=0, delta_y=8), NodeToWire(wire_in_tile_pkey=18956, delta_x=0, delta_y=47), NodeToWire(wire_in_tile_pkey=18954, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=3057, delta_x=0, delta_y=60)}))
               (84994, frozenset({NodeToWire(wire_in_tile_pkey=57346, delta_x=70, delta_y=0)}))
               (85029, frozenset({NodeToWire(wire_in_tile_pkey=45985, delta_x=0, delta_y=17)}))
               (84996, frozenset({NodeToWire(wire_in_tile_pkey=57348, delta_x=70, delta_y=0)}))
               (85031, frozenset({NodeToWire(wire_in_tile_pkey=45983, delta_x=0, delta_y=17)}))
               (84990, frozenset({NodeToWire(wire_in_tile_pkey=57342, delta_x=70, delta_y=0)}))
               (85030, frozenset({NodeToWire(wire_in_tile_pkey=45981, delta_x=0, delta_y=17)}))
               (85000, frozenset({NodeToWire(wire_in_tile_pkey=57352, delta_x=70, delta_y=0)}))
               (84995, frozenset({NodeToWire(wire_in_tile_pkey=57347, delta_x=70, delta_y=0)}))
               (84999, frozenset({NodeToWire(wire_in_tile_pkey=57351, delta_x=70, delta_y=0)}))
               (84989, frozenset({NodeToWire(wire_in_tile_pkey=57341, delta_x=70, delta_y=0)}))
               (85044, frozenset({NodeToWire(wire_in_tile_pkey=43566, delta_x=0, delta_y=-18)}))
               (85002, frozenset({NodeToWire(wire_in_tile_pkey=57354, delta_x=70, delta_y=0)}))
               (84993, frozenset({NodeToWire(wire_in_tile_pkey=57345, delta_x=70, delta_y=0)}))
               (85041, frozenset({NodeToWire(wire_in_tile_pkey=11307, delta_x=-7, delta_y=0)}))
               (84998, frozenset({NodeToWire(wire_in_tile_pkey=57350, delta_x=70, delta_y=0)}))
               (84937, frozenset({NodeToWire(wire_in_tile_pkey=18957, delta_x=0, delta_y=47), NodeToWire(wire_in_tile_pkey=18955, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=3058, delta_x=0, delta_y=60), NodeToWire(wire_in_tile_pkey=3056, delta_x=0, delta_y=8)}))
    s is one biclique and is a tuple (setOfTiles, setOfNodeToWire)
         Tiles:
               Tile(tile_pkey=9714)
         NodeToWires:
               (85046, frozenset({NodeToWire(wire_in_tile_pkey=43568, delta_x=0, delta_y=-18)}))
               (85040, frozenset({NodeToWire(wire_in_tile_pkey=11306, delta_x=-7, delta_y=0)}))
               (85042, frozenset({NodeToWire(wire_in_tile_pkey=11308, delta_x=-7, delta_y=0)}))
               (84936, frozenset({NodeToWire(wire_in_tile_pkey=18958, delta_x=0, delta_y=-57), NodeToWire(wire_in_tile_pkey=3059, delta_x=0, delta_y=-44), NodeToWire(wire_in_tile_pkey=18956, delta_x=0, delta_y=47), NodeToWire(wire_in_tile_pkey=18954, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=3057, delta_x=0, delta_y=60), NodeToWire(wire_in_tile_pkey=3055, delta_x=0, delta_y=8)}))
               (84997, frozenset({NodeToWire(wire_in_tile_pkey=57349, delta_x=70, delta_y=0)}))
               (85001, frozenset({NodeToWire(wire_in_tile_pkey=57353, delta_x=70, delta_y=0)}))
               (84991, frozenset({NodeToWire(wire_in_tile_pkey=57343, delta_x=70, delta_y=0)}))
               (85045, frozenset({NodeToWire(wire_in_tile_pkey=43567, delta_x=0, delta_y=-18)}))
               (85043, frozenset({NodeToWire(wire_in_tile_pkey=11309, delta_x=-7, delta_y=0)}))
               (84992, frozenset({NodeToWire(wire_in_tile_pkey=57344, delta_x=70, delta_y=0)}))
               (84994, frozenset({NodeToWire(wire_in_tile_pkey=57346, delta_x=70, delta_y=0)}))
               (85029, frozenset({NodeToWire(wire_in_tile_pkey=45985, delta_x=0, delta_y=17)}))
               (84996, frozenset({NodeToWire(wire_in_tile_pkey=57348, delta_x=70, delta_y=0)}))
               (85031, frozenset({NodeToWire(wire_in_tile_pkey=45983, delta_x=0, delta_y=17)}))
               (84990, frozenset({NodeToWire(wire_in_tile_pkey=57342, delta_x=70, delta_y=0)}))
               (85030, frozenset({NodeToWire(wire_in_tile_pkey=45981, delta_x=0, delta_y=17)}))
               (85000, frozenset({NodeToWire(wire_in_tile_pkey=57352, delta_x=70, delta_y=0)}))
               (84995, frozenset({NodeToWire(wire_in_tile_pkey=57347, delta_x=70, delta_y=0)}))
               (84937, frozenset({NodeToWire(wire_in_tile_pkey=3056, delta_x=0, delta_y=8), NodeToWire(wire_in_tile_pkey=18955, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=3060, delta_x=0, delta_y=-44), NodeToWire(wire_in_tile_pkey=18957, delta_x=0, delta_y=47), NodeToWire(wire_in_tile_pkey=3058, delta_x=0, delta_y=60), NodeToWire(wire_in_tile_pkey=18959, delta_x=0, delta_y=-57)}))
               (84999, frozenset({NodeToWire(wire_in_tile_pkey=57351, delta_x=70, delta_y=0)}))
               (84989, frozenset({NodeToWire(wire_in_tile_pkey=57341, delta_x=70, delta_y=0)}))
               (85044, frozenset({NodeToWire(wire_in_tile_pkey=43566, delta_x=0, delta_y=-18)}))
               (85002, frozenset({NodeToWire(wire_in_tile_pkey=57354, delta_x=70, delta_y=0)}))
               (84993, frozenset({NodeToWire(wire_in_tile_pkey=57345, delta_x=70, delta_y=0)}))
               (85041, frozenset({NodeToWire(wire_in_tile_pkey=11307, delta_x=-7, delta_y=0)}))
               (84998, frozenset({NodeToWire(wire_in_tile_pkey=57350, delta_x=70, delta_y=0)}))
    s is one biclique and is a tuple (setOfTiles, setOfNodeToWire)
         Tiles:
               Tile(tile_pkey=9713)
               Tile(tile_pkey=9714)
         NodeToWires:
               (85044, frozenset({NodeToWire(wire_in_tile_pkey=43566, delta_x=0, delta_y=-18)}))
               (85030, frozenset({NodeToWire(wire_in_tile_pkey=45981, delta_x=0, delta_y=17)}))
               (85046, frozenset({NodeToWire(wire_in_tile_pkey=43568, delta_x=0, delta_y=-18)}))
               (85040, frozenset({NodeToWire(wire_in_tile_pkey=11306, delta_x=-7, delta_y=0)}))
               (84936, frozenset({NodeToWire(wire_in_tile_pkey=18958, delta_x=0, delta_y=-57), NodeToWire(wire_in_tile_pkey=3059, delta_x=0, delta_y=-44), NodeToWire(wire_in_tile_pkey=18956, delta_x=0, delta_y=47), NodeToWire(wire_in_tile_pkey=18954, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=3057, delta_x=0, delta_y=60), NodeToWire(wire_in_tile_pkey=3055, delta_x=0, delta_y=8)}))
               (85042, frozenset({NodeToWire(wire_in_tile_pkey=11308, delta_x=-7, delta_y=0)}))
               (85041, frozenset({NodeToWire(wire_in_tile_pkey=11307, delta_x=-7, delta_y=0)}))
               (85029, frozenset({NodeToWire(wire_in_tile_pkey=45985, delta_x=0, delta_y=17)}))
               (85043, frozenset({NodeToWire(wire_in_tile_pkey=11309, delta_x=-7, delta_y=0)}))
               (84937, frozenset({NodeToWire(wire_in_tile_pkey=3056, delta_x=0, delta_y=8), NodeToWire(wire_in_tile_pkey=18955, delta_x=0, delta_y=-5), NodeToWire(wire_in_tile_pkey=3060, delta_x=0, delta_y=-44), NodeToWire(wire_in_tile_pkey=18957, delta_x=0, delta_y=47), NodeToWire(wire_in_tile_pkey=3058, delta_x=0, delta_y=60), NodeToWire(wire_in_tile_pkey=18959, delta_x=0, delta_y=-57)}))
               (85031, frozenset({NodeToWire(wire_in_tile_pkey=45983, delta_x=0, delta_y=17)}))
               (85045, frozenset({NodeToWire(wire_in_tile_pkey=43567, delta_x=0, delta_y=-18)}))
    s is one biclique and is a tuple (setOfTiles, setOfNodeToWire)
         Tiles:
               Tile(tile_pkey=9715)
               Tile(tile_pkey=9712)
               Tile(tile_pkey=9713)
               Tile(tile_pkey=9714)
         NodeToWires:
               (85044, frozenset({NodeToWire(wire_in_tile_pkey=43566, delta_x=0, delta_y=-18)}))
               (85030, frozenset({NodeToWire(wire_in_tile_pkey=45981, delta_x=0, delta_y=17)}))
               (85046, frozenset({NodeToWire(wire_in_tile_pkey=43568, delta_x=0, delta_y=-18)}))
               (85040, frozenset({NodeToWire(wire_in_tile_pkey=11306, delta_x=-7, delta_y=0)}))
               (85042, frozenset({NodeToWire(wire_in_tile_pkey=11308, delta_x=-7, delta_y=0)}))
               (85041, frozenset({NodeToWire(wire_in_tile_pkey=11307, delta_x=-7, delta_y=0)}))
               (85029, frozenset({NodeToWire(wire_in_tile_pkey=45985, delta_x=0, delta_y=17)}))
               (85043, frozenset({NodeToWire(wire_in_tile_pkey=11309, delta_x=-7, delta_y=0)}))
               (85031, frozenset({NodeToWire(wire_in_tile_pkey=45983, delta_x=0, delta_y=17)}))
               (85045, frozenset({NodeToWire(wire_in_tile_pkey=43567, delta_x=0, delta_y=-18)}))
5 complete subgraphs required for solution
| |        #                                                                                                        | 3 Elapsed Time: 0:00:00
Have 4 tile patterns
Max 2 patterns
Number of tile pattern elements: 6
Printing node_wire_tile_pkeys_array: len= 26
   0 84936
   1 84937
   2 84989
   3 84990
   4 84991
   5 84992
   6 84993
   7 84994
   8 84995
   9 84996
   10 84997
   11 84998
   12 84999
   13 85000
   14 85001
   15 85002
   16 85029
   17 85030
   18 85031
   19 85040
   20 85041
   21 85042
   22 85043
   23 85044
   24 85045
   25 85046
Wire patterns:  len= 50
   0 11306 -7, 0
   1 11307 -7, 0
   2 11308 -7, 0
   3 11309 -7, 0
   4 18958 0, -57
   5 18959 0, -57
   6 3059 0, -44
   7 3060 0, -44
   8 43566 0, -18
   9 43567 0, -18
   10 43568 0, -18
   11 18954 0, -5
   12 18955 0, -5
   13 3055 0, 8
   14 3056 0, 8
   15 45981 0, 17
   16 45983 0, 17
   17 45985 0, 17
   18 18956 0, 47
   19 18957 0, 47
   20 3057 0, 60
   21 3058 0, 60
   22 55201 70, 0
   23 55202 70, 0
   24 55203 70, 0
   25 55204 70, 0
   26 55205 70, 0
   27 55206 70, 0
   28 55207 70, 0
   29 55208 70, 0
   30 55209 70, 0
   31 55210 70, 0
   32 55211 70, 0
   33 55212 70, 0
   34 55213 70, 0
   35 55214 70, 0
   36 57341 70, 0
   37 57342 70, 0
   38 57343 70, 0
   39 57344 70, 0
   40 57345 70, 0
   41 57346 70, 0
   42 57347 70, 0
   43 57348 70, 0
   44 57349 70, 0
   45 57350 70, 0
   46 57351 70, 0
   47 57352 70, 0
   48 57353 70, 0
   49 57354 70, 0

####Node_patterns_data has 44 entries
Node_patterns_data:  len= 44
  0 (10,)
  1 (0,)
  2 (2,)
  3 (44,)
  4 (48,)
  5 (38,)
  6 (9,)
  7 (3,)
  8 (39,)
  9 (41,)
  10 (17,)
  11 (43,)
  12 (16,)
  13 (37,)
  14 (15,)
  15 (47,)
  16 (42,)
  17 (46,)
  18 (36,)
  19 (8,)
  20 (49,)
  21 (40,)
  22 (1,)
  23 (45,)
  24 (5, 7, 12, 14)
  25 (23,)
  26 (28,)
  27 (4, 6, 11, 13)
  28 (31,)
  29 (25,)
  30 (29,)
  31 (30,)
  32 (32,)
  33 (24,)
  34 (22,)
  35 (27,)
  36 (34,)
  37 (35,)
  38 (33,)
  39 (26,)
  40 (11, 13, 18, 20)
  41 (12, 14, 19, 21)
  42 (4, 6, 11, 13, 18, 20)
  43 (5, 7, 12, 14, 19, 21)
####Node_patterns_data[43] contains 6 entries

####Subgraph[1] contains 26 entries is for tile 9712
####In sorted order they are: 0, 1, 2, 6, 7, 10, 12, 14, 19, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39
Subgraphs:  len= 5
  0: [None, None, 18, 13, 5, 8, 21, 9, 16, 11, 3, 23, 17, 15, 4, 20, 10, 14, 12, 1, 22, 2, 7, 19, 6, 0]
  1: [27, 24, 34, 25, 33, 29, 39, 35, 26, 30, 31, 28, 32, 38, 36, 37, 10, 14, 12, 1, 22, 2, 7, 19, 6, 0]
  2: [None, None, 34, 25, 33, 29, 39, 35, 26, 30, 31, 28, 32, 38, 36, 37, 10, 14, 12, 1, 22, 2, 7, 19, 6, 0]
  3: [40, 41, 18, 13, 5, 8, 21, 9, 16, 11, 3, 23, 17, 15, 4, 20, 10, 14, 12, 1, 22, 2, 7, 19, 6, 0]
  4: [42, 43, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 10, 14, 12, 1, 22, 2, 7, 19, 6, 0]

####Tile 9712 maps to tile_patterns[2] which is subgraph[1]
####Tile 9713 and tile 9714 share subgraph[4]
####Tile 9713 also maps to subgraph[2]
####Tile 9714 also maps to subgraph[0]
####Tile 9715 maps to subgraph[3]
Tile_patterns_data:  len= 4
 0 (3,)
 1 (4, 2)
 2 (1,)
 3 (4, 0)
Tile_to_tile_patterns:  len= 2
  0 [9712, 9713, 9714, 9715]
  1 [2, 1, 3, 0]
Size on disk:  2032

1. Find the patterns in a tile
####Tile 9712 maps to tile_patterns[2] which is subgraph[1]
####Subgraph[1] (and all other subgraphs) contain 26 entries, one for each node from this tile
####Subgraph[1]: [27, 24, 34, 25, 33, 29, 39, 35, 26, 30, 31, 28, 32, 38, 36, 37, 10, 14, 12, 1, 22, 2, 7, 19, 6, 0]
    ####For Subgraph[1][0]:
        ####node_wire_tile_pkeys_array[0]=84936 - this is the node's first wire (alias for node since node #'s never show up)
        ####Subgraph[1][0]=27, Node_patterns_data[27]=(4, 6, 11, 13)
            ####wire_patterns[4]=18958 0, -57
            ####wire_patterns[6]=3059 0, -44
            ####wire_patterns[11]=18954 0, -5
            ####wire_patterns[13]=3055 0, 8
    #### This matches (from above): (9712, 84936, [(18958, 0, -57), (3059, 0, -44), (3055, 0, 8), (18954, 0, -5)])
                                     tile   nwit     nwit  dx, dy
####Can repeat the above steps for remaining subgraph entries 1-25 to learn about other nodes

2. I am node=n in tile=t, what wires in me lead to pips I can drive?
####Node 84936 is entry 0 in node_wire_tile_pkeys_array  
    - REQUIRES SEARCH TO FIND unless 84936 is actually known by its index of 0 so you can do a direct lookup in table
####Find tile in Tile_to_tile_patterns[0] and use position to look in Tile_to_tile_patterns[1] to get a Tile_patterns_data index 
    - REQUIRES SEARCH TO FIND unless 9712 is known by its index of 0 so you can do do a direct lookup in table
####Using that index, look in Tile_patterns_data to get set of subgraphs I may appear in
    - In the example above, 84936 (index 0) does not appear in subgraphs 0 or 2
    - In both those cases is paired up with subgraph 4 which does have index 0
####Look through each subgraph[i][0] to see if there is a None or a number there
    ####If there is a number (i), find Node_patterns_data[i] and from that look up the actual pattern in wire_patterns

