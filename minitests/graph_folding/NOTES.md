After building the database, the basic algorithm:
    - foreach tile type:
        - reduce_graph_for_type.py --node_to_wires -only_pips 
        - reduce_graph_for_type.py --wire_to_node
        - reduce_graph_for_type.py --node_to_wires


## --node_to_wires --only_pips


Tiles for tile_types
*   3 = 2 CLK_TERM        (none)
*  10 = 2 GTP_CHANNEL_2   (huge)
*  13 = 1 CLK_PMV         (3)
*  16 = 2 HCLK_CMT_L      (26)
*  22 = 1 HCLK_L_BOT_UTURN
*  41 = 2 BRKH_GTX         (none)
*  42 = 2 CMT_TOP_L_LOWER_T (huge)
*  44 = 1
*  48 = 2 HCLK_TERM_GTX   (none)
*  49 = 1 CLK_PMV2 
*  58 = 2 CMT_TOP_L_UPPER_T   (huge)
*  62 = 1 CLK_PMV2_SVT
*  71 = 1 CLK_MTBF2
*  73 = 1 CLK_BUFG_TOP_R
*  77 = 1 CFG_CENTER_BOT
*  78 = 2 TERM_CMT                (none)
*  81 = 2 CLK_HROW_BOT_R      (huge)
*  82 = 2 CLK_HROW_TOP_R      (huge)
*  86 = 2 CMT_TOP_L_LOWER_B   (huge)
*  87 = 2 GTP_CHANNEL_3      (huge)
*  90 = 1 MONITOR_BOT
*  94 = 1 CLK_PMVIOB
* 103 = 1 CFG_CENTER_MID
* 110 = 2 GTP_CHANNEL_0    (huge)
* 111 = 2 GTP_COMMON         (big)
* 112 = 1 CLK_BUFG_BOT_R
* 113 = 2 HCLK_GTX    (none)
* 115 = 1 MONITOR_TOP
* 118 = 1 HCLK_R_BOT_UTURN
* 120 = 2 CMT_TOP_L_UPPER_B   (huge)
* 121 = 1 PCIE_BOT
* 125 = 1 CFG_CENTER_TOP
* 126 = 2 GTP_CHANNEL_1  (huge)
* 127 = 1 PCIE_TOP

SELECT count(tile.pkey) as tileKey, tile_type.pkey as tileType, tile_type.name as tileName 
FROM tile INNER JOIN tile_type ON tile.tile_type_pkey=tile_type.pkey
group by tileType

1	13	CLK_PMV
1	22	HCLK_L_BOT_UTURN
1	44	MONITOR_MID
1	49	CLK_PMV2
1	62	CLK_PMV2_SVT
1	71	CLK_MTBF2
1	73	CLK_BUFG_TOP_R
1	77	CFG_CENTER_BOT
1	90	MONITOR_BOT
1	94	CLK_PMVIOB
1	103	CFG_CENTER_MID
1	112	CLK_BUFG_BOT_R
1	115	MONITOR_TOP
1	118	HCLK_R_BOT_UTURN
1	121	PCIE_BOT
1	125	CFG_CENTER_TOP
1	127	PCIE_TOP
2	3	CLK_TERM
2	10	GTP_CHANNEL_2
2	16	HCLK_CMT_L
2	41	BRKH_GTX
2	42	CMT_TOP_L_LOWER_T
2	48	HCLK_TERM_GTX
2	58	CMT_TOP_L_UPPER_T
2	78	TERM_CMT
2	81	CLK_HROW_BOT_R
2	82	CLK_HROW_TOP_R
2	86	CMT_TOP_L_LOWER_B
2	87	GTP_CHANNEL_3
2	110	GTP_CHANNEL_0
2	111	GTP_COMMON
2	113	HCLK_GTX
2	120	CMT_TOP_L_UPPER_B
2	126	GTP_CHANNEL_1
3	70	BRKH_CLK  (no nodes driving pips)
3	116	BRKH_DSP_L  (no nodes driving pips)
4	9	CMT_TOP_R_LOWER_T   (all 4 share identical patterns)
4	14	BRKH_CMT  (no nodes driving pips)
4	18	CMT_PMV_L  (no nodes driving pips)
4	31	HCLK_DSP_L (no nodes driving pips)
4	35	RIOI3_SING   (all 4 share identical patterns)
4	38	CMT_TOP_R_UPPER_B  (211 wires, one pattern)
4	46	HCLK_VFRAME (no nodes driving pips)
4	51	RIOI3_TBYTETERM  (all sharing one pattern)
4	55	RIOB33_SING (all share one pattern)
4	72	CMT_TOP_R_UPPER_T
4	75	CMT_TOP_R_LOWER_B
4	106	HCLK_CMT   (??? 4 different patterns.  BUT, some of them have None entries.  The tile_patterns_data have multiple entries which fit together
6	1	BRKH_DSP_R (no nodes driving pips)
6	24	HCLK_IOI3  (Has 8 subgraphs, 2 of which are unused and have some Nones)
6	29	HCLK_TERM  (no nodes driving pips)
6	34	HCLK_FIFO_L (no nodes driving pips)
6	96	HCLK_IOB (no nodes driving pips)
8	20	LIOI3_SING (all share one pattern)
8	36	CMT_PMV (no nodes driving pips)
8	69	RIOI3_TBYTESRC
8	80	LIOB33_SING
8	83	HCLK_DSP_R (no nodes driving pips)
8	100	CLK_BUFG_REBUF
8	102	LIOI3_TBYTETERM
8	105	CMT_FIFO_L
9	89	BRKH_BRAM
11	85	HCLK_FEEDTHRU_1 (none)
12	12	BRKH_B_TERM_INT
12	95	HCLK_FEEDTHRU_2
14	64	HCLK_BRAM (none)
14	128	BRKH_TERM_INT
16	33	CMT_FIFO_R
16	98	LIOI3_TBYTESRC
20	119	BRAM_R (5 patterns, some with None)
25	40	PCIE_INT_INTERFACE_L
25	57	PCIE_INT_INTERFACE_R
36	104	RIOI3
40	107	DSP_L (all share one)
48	26	HCLK_VBRK
48	84	HCLK_INT_INTERFACE
48	124	RIOB33
52	39	B_TERM_INT
52	53	T_TERM_INT
72	91	LIOI3
80	93	DSP_R
96	43	LIOB33
100	8	IO_INT_INTERFACE_R
100	19	BRAM_INT_INTERFACE_R
100	45	VBRK_EXT
100	60	R_TERM_INT
100	74	R_TERM_INT_GTX
100	99	GTP_INT_INTERFACE  (50 patterns, lots of None)
103	50	HCLK_L
103	79	HCLK_R  (all share one)
106	4	BRKH_CLB
115	37	BRAM_L
123	15	PCIE_NULL
133	108	CLK_FEED
142	67	BRKH_INT
160	32	HCLK_CLB
200	52	IO_INT_INTERFACE_L
200	61	L_TERM_INT
200	66	VFRAME (none)
500	114	INT_INTERFACE_L
525	25	INT_FEEDTHRU_1
575	30	BRAM_INT_INTERFACE_L (all share one)
600	21	INT_FEEDTHRU_2
800	97	INT_INTERFACE_R (all share one)
1475	6	CLBLL_L (all share one)
1700	27	CLBLL_R
2350	11	CLBLM_R
2400	23	VBRK
2400	54	CLBLM_L (all share one)
4127	101	NULL (none)
5175	7	INT_R  (~200 nodes per tile, 
            Tile, Node, Wire, dx, dy
            Node wires: 182
            Max number of patterns: 2
            Minimum number of pattern storage: 3490
            Unique wire in tile pkey 2149
            Unique node_to_wires 3223
            Unique patterns 3324
            Unique dx dy 240
            Unique dx dy dist 45
            density = 0.05293546835021831, beta = 0.5, P = 0.26759173509295053, N = 166790.25
            Found 2353 possible complete subgraphs
            462 complete subgraphs required for solution

            Have 1910 tile patterns
            Max 10 patterns
            Number of tile pattern elements: 11487

            node_wire_tile_pkeys_array has 182 entries

            There are > 6,500 Wire patterns

            Tile_patterns_data has 1910 entries
            461 subgraphs


5175	17	INT_L
#########################################
6	1	BRKH_DSP_R
2	3	CLK_TERM
106	4	BRKH_CLB
1475	6	CLBLL_L
5175	7	INT_R
100	8	IO_INT_INTERFACE_R
4	9	CMT_TOP_R_LOWER_T
2	10	GTP_CHANNEL_2
2350	11	CLBLM_R
12	12	BRKH_B_TERM_INT
1	13	CLK_PMV
4	14	BRKH_CMT
123	15	PCIE_NULL
2	16	HCLK_CMT_L
5175	17	INT_L
4	18	CMT_PMV_L
100	19	BRAM_INT_INTERFACE_R
8	20	LIOI3_SING
600	21	INT_FEEDTHRU_2
1	22	HCLK_L_BOT_UTURN
2400	23	VBRK
6	24	HCLK_IOI3
525	25	INT_FEEDTHRU_1
48	26	HCLK_VBRK
1700	27	CLBLL_R
6	29	HCLK_TERM
575	30	BRAM_INT_INTERFACE_L
4	31	HCLK_DSP_L
160	32	HCLK_CLB
16	33	CMT_FIFO_R
6	34	HCLK_FIFO_L
4	35	RIOI3_SING
8	36	CMT_PMV
115	37	BRAM_L
4	38	CMT_TOP_R_UPPER_B
52	39	B_TERM_INT
25	40	PCIE_INT_INTERFACE_L
2	41	BRKH_GTX
2	42	CMT_TOP_L_LOWER_T
96	43	LIOB33
1	44	MONITOR_MID
100	45	VBRK_EXT
4	46	HCLK_VFRAME
2	48	HCLK_TERM_GTX
1	49	CLK_PMV2
103	50	HCLK_L
4	51	RIOI3_TBYTETERM
200	52	IO_INT_INTERFACE_L
52	53	T_TERM_INT
2400	54	CLBLM_L
4	55	RIOB33_SING
25	57	PCIE_INT_INTERFACE_R
2	58	CMT_TOP_L_UPPER_T
100	60	R_TERM_INT
200	61	L_TERM_INT
1	62	CLK_PMV2_SVT
14	64	HCLK_BRAM
200	66	VFRAME
142	67	BRKH_INT
8	69	RIOI3_TBYTESRC
3	70	BRKH_CLK
1	71	CLK_MTBF2
4	72	CMT_TOP_R_UPPER_T
1	73	CLK_BUFG_TOP_R
100	74	R_TERM_INT_GTX
4	75	CMT_TOP_R_LOWER_B
1	77	CFG_CENTER_BOT
2	78	TERM_CMT
103	79	HCLK_R
8	80	LIOB33_SING
2	81	CLK_HROW_BOT_R
2	82	CLK_HROW_TOP_R
8	83	HCLK_DSP_R
48	84	HCLK_INT_INTERFACE
11	85	HCLK_FEEDTHRU_1
2	86	CMT_TOP_L_LOWER_B
2	87	GTP_CHANNEL_3
9	89	BRKH_BRAM
1	90	MONITOR_BOT
72	91	LIOI3
80	93	DSP_R
1	94	CLK_PMVIOB
12	95	HCLK_FEEDTHRU_2
6	96	HCLK_IOB
800	97	INT_INTERFACE_R
16	98	LIOI3_TBYTESRC
100	99	GTP_INT_INTERFACE
8	100	CLK_BUFG_REBUF
4127	101	NULL
8	102	LIOI3_TBYTETERM
1	103	CFG_CENTER_MID
36	104	RIOI3
8	105	CMT_FIFO_L
4	106	HCLK_CMT
40	107	DSP_L
133	108	CLK_FEED
2	110	GTP_CHANNEL_0
2	111	GTP_COMMON
1	112	CLK_BUFG_BOT_R
2	113	HCLK_GTX
500	114	INT_INTERFACE_L
1	115	MONITOR_TOP
3	116	BRKH_DSP_L
1	118	HCLK_R_BOT_UTURN
20	119	BRAM_R
2	120	CMT_TOP_L_UPPER_B
1	121	PCIE_BOT
48	124	RIOB33
1	125	CFG_CENTER_TOP
2	126	GTP_CHANNEL_1
1	127	PCIE_TOP
14	128	BRKH_TERM_INT

#######################################################################################
## -wires_to_nodes
1	13	CLK_PMV
1	22	HCLK_L_BOT_UTURN
1	44	MONITOR_MID
1	49	CLK_PMV2
1	62	CLK_PMV2_SVT
1	71	CLK_MTBF2
1	73	CLK_BUFG_TOP_R
1	77	CFG_CENTER_BOT
1	90	MONITOR_BOT
1	94	CLK_PMVIOB
1	103	CFG_CENTER_MID
1	112	CLK_BUFG_BOT_R
1	115	MONITOR_TOP
1	118	HCLK_R_BOT_UTURN
1	121	PCIE_BOT
1	125	CFG_CENTER_TOP
1	127	PCIE_TOP
2	3	CLK_TERM  (2 tiles, totally disjoint patterns)
2	10	GTP_CHANNEL_2
2	16	HCLK_CMT_L
2	41	BRKH_GTX
2	42	CMT_TOP_L_LOWER_T
2	48	HCLK_TERM_GTX
2	58	CMT_TOP_L_UPPER_T
2	78	TERM_CMT
2	81	CLK_HROW_BOT_R
2	82	CLK_HROW_TOP_R
2	86	CMT_TOP_L_LOWER_B
2	87	GTP_CHANNEL_3
2	110	GTP_CHANNEL_0
2	111	GTP_COMMON
2	113	HCLK_GTX
2	120	CMT_TOP_L_UPPER_B
2	126	GTP_CHANNEL_1
3	70	BRKH_CLK  
3	116	BRKH_DSP_L  (all 3 identical)
4	9	CMT_TOP_R_LOWER_T   
4	14	BRKH_CMT  
4	18	CMT_PMV_L  
4	31	HCLK_DSP_L 
4	35	RIOI3_SING          (2 patterns with 2 tiles each.  One of the patterns has lots of nones)
4	38	CMT_TOP_R_UPPER_B 
4	46	HCLK_VFRAME 
4	51	RIOI3_TBYTETERM  
4	55	RIOB33_SING 
4	72	CMT_TOP_R_UPPER_T
4	75	CMT_TOP_R_LOWER_B
4	106	HCLK_CMT   
6	1	BRKH_DSP_R 
6	24	HCLK_IOI3  (4 patterns for 6 tiles)
6	29	HCLK_TERM  
6	34	HCLK_FIFO_L 
6	96	HCLK_IOB 
8	20	LIOI3_SING 
8	36	CMT_PMV
8	69	RIOI3_TBYTESRC
8	80	LIOB33_SING
8	83	HCLK_DSP_R 
8	100	CLK_BUFG_REBUF  (7 patterns, some have multiples)
8	102	LIOI3_TBYTETERM
8	105	CMT_FIFO_L
9	89	BRKH_BRAM
11	85	HCLK_FEEDTHRU_1 
12	12	BRKH_B_TERM_INT
12	95	HCLK_FEEDTHRU_2
14	64	HCLK_BRAM 
14	128	BRKH_TERM_INT
16	33	CMT_FIFO_R
16	98	LIOI3_TBYTESRC
20	119	BRAM_R               (13 patterns, some have multiples)
25	40	PCIE_INT_INTERFACE_L
25	57	PCIE_INT_INTERFACE_R
36	104	RIOI3
40	107	DSP_L      (21 patterns, lots of multiples)
48	26	HCLK_VBRK
48	84	HCLK_INT_INTERFACE
48	124	RIOB33
52	39	B_TERM_INT
52	53	T_TERM_INT
72	91	LIOI3
80	93	DSP_R   (28 patterns)
96	43	LIOB33
100	8	IO_INT_INTERFACE_R
100	19	BRAM_INT_INTERFACE_R
100	45	VBRK_EXT
100	60	R_TERM_INT
100	74	R_TERM_INT_GTX
100	99	GTP_INT_INTERFACE 
103	50	HCLK_L
103	79	HCLK_R 
106	4	BRKH_CLB
115	37	BRAM_L
123	15	PCIE_NULL
133	108	CLK_FEED
142	67	BRKH_INT
160	32	HCLK_CLB
200	52	IO_INT_INTERFACE_L
200	61	L_TERM_INT
200	66	VFRAME 
500	114	INT_INTERFACE_L
525	25	INT_FEEDTHRU_1
575	30	BRAM_INT_INTERFACE_L 
600	21	INT_FEEDTHRU_2
800	97	INT_INTERFACE_R 
1475	6	CLBLL_L 
1700	27	CLBLL_R
2350	11	CLBLM_R
2400	23	VBRK
2400	54	CLBLM_L 
4127	101	NULL 
5175	7	INT_R 
5175	17	INT_L

#######################################################################################
## -nodes_to_wires
1	13	CLK_PMV
1	22	HCLK_L_BOT_UTURN
1	44	MONITOR_MID
1	49	CLK_PMV2
1	62	CLK_PMV2_SVT
1	71	CLK_MTBF2
1	73	CLK_BUFG_TOP_R
1	77	CFG_CENTER_BOT
1	90	MONITOR_BOT
1	94	CLK_PMVIOB
1	103	CFG_CENTER_MID
1	112	CLK_BUFG_BOT_R
1	115	MONITOR_TOP
1	118	HCLK_R_BOT_UTURN
1	121	PCIE_BOT
1	125	CFG_CENTER_TOP
1	127	PCIE_TOP
2	3	CLK_TERM  (2 tiles, totally disjoint patterns)
2	10	GTP_CHANNEL_2
2	16	HCLK_CMT_L
2	41	BRKH_GTX
2	42	CMT_TOP_L_LOWER_T
2	48	HCLK_TERM_GTX
2	58	CMT_TOP_L_UPPER_T
2	78	TERM_CMT
2	81	CLK_HROW_BOT_R
2	82	CLK_HROW_TOP_R
2	86	CMT_TOP_L_LOWER_B
2	87	GTP_CHANNEL_3
2	110	GTP_CHANNEL_0
2	111	GTP_COMMON
2	113	HCLK_GTX
2	120	CMT_TOP_L_UPPER_B
2	126	GTP_CHANNEL_1
3	70	BRKH_CLK  
3	116	BRKH_DSP_L  (all 3 identical)
4	9	CMT_TOP_R_LOWER_T   
4	14	BRKH_CMT  
4	18	CMT_PMV_L  
4	31	HCLK_DSP_L 
4	35	RIOI3_SING          (2 patterns with 2 tiles each.  One of the patterns has lots of nones)
4	38	CMT_TOP_R_UPPER_B 
4	46	HCLK_VFRAME 
4	51	RIOI3_TBYTETERM  
4	55	RIOB33_SING 
4	72	CMT_TOP_R_UPPER_T
4	75	CMT_TOP_R_LOWER_B
4	106	HCLK_CMT   
6	1	BRKH_DSP_R 
6	24	HCLK_IOI3  (4 patterns for 6 tiles)
6	29	HCLK_TERM  
6	34	HCLK_FIFO_L 
6	96	HCLK_IOB 
8	20	LIOI3_SING 
8	36	CMT_PMV
8	69	RIOI3_TBYTESRC
8	80	LIOB33_SING
8	83	HCLK_DSP_R 
8	100	CLK_BUFG_REBUF  (7 patterns, some have multiples)
8	102	LIOI3_TBYTETERM
8	105	CMT_FIFO_L
9	89	BRKH_BRAM
11	85	HCLK_FEEDTHRU_1 
12	12	BRKH_B_TERM_INT
12	95	HCLK_FEEDTHRU_2
14	64	HCLK_BRAM 
14	128	BRKH_TERM_INT
16	33	CMT_FIFO_R
16	98	LIOI3_TBYTESRC
20	119	BRAM_R               (13 patterns, some have multiples)
25	40	PCIE_INT_INTERFACE_L
25	57	PCIE_INT_INTERFACE_R
36	104	RIOI3
40	107	DSP_L      (21 patterns, lots of multiples)
48	26	HCLK_VBRK
48	84	HCLK_INT_INTERFACE
48	124	RIOB33
52	39	B_TERM_INT
52	53	T_TERM_INT
72	91	LIOI3
80	93	DSP_R   (28 patterns)
96	43	LIOB33
100	8	IO_INT_INTERFACE_R
100	19	BRAM_INT_INTERFACE_R
100	45	VBRK_EXT
100	60	R_TERM_INT
100	74	R_TERM_INT_GTX
100	99	GTP_INT_INTERFACE 
103	50	HCLK_L
103	79	HCLK_R 
106	4	BRKH_CLB
115	37	BRAM_L
123	15	PCIE_NULL
133	108	CLK_FEED
142	67	BRKH_INT
160	32	HCLK_CLB
200	52	IO_INT_INTERFACE_L
200	61	L_TERM_INT
200	66	VFRAME 
500	114	INT_INTERFACE_L
525	25	INT_FEEDTHRU_1
575	30	BRAM_INT_INTERFACE_L 
600	21	INT_FEEDTHRU_2
800	97	INT_INTERFACE_R 
1475	6	CLBLL_L 
1700	27	CLBLL_R
2350	11	CLBLM_R
2400	23	VBRK
2400	54	CLBLM_L 
4127	101	NULL 
5175	7	INT_R 
5175	17	INT_L

############################################################################################
Questions for Keith
I understand that:
1. Phase 1 gets mapping from nodes to downhill pips in other cells (actually the wires driving pips)
    - A node has a "home tile" which is the tile where its "node source wire" is located.  Right?
    - What is a "node source wire".  It seems  obvious that if that wire is driven by an input pin or BEL output that it is a "source" wire.
    - Can there be more than one source wire per node?
    - Besides inputs to sites, outputs from BEL pins, outputs from PIPs what else can constitute a node source wire?
    - I doubt it is that clean.  Doesn't the same wire participate in lots of pips?  Doesn't bidirectional PIPs mess things up?
2. Phase 2 gets mapping from wires to nodes they are a part of.  
    - For a given tile, the mapping pattern is given.  
    - Many tiles can share the same pattern.  
    - In some patterns there are None entries.
    - Some tile_patterns_data consist of multiple patterns.  How do multiple sub-patterns combine to make one pattern?
3. Phase 3 gets mapping from nodes to wires in other cells but not in same cell?
    - For CLK_PMV I get same results - shouldn't I get intermediate wires as well?
    - Trying to reproduce this in Tcl I get tons of wires (instead of the 3 I get with this code)
        - It looks like intermediate wires have been trimmed out?
4. Some subgraphs have None entries and some tile_patterns_data have multiple values per entry
6. These .bin files are not ready for VPR and VPR is not ready for them?
7. Meaning of has_pip_from - confirm.

###############################################################################################
More questions for Keith:
1. These examples elide the middle wires in nodes.  How will that work with timing model?  
2. Will intermediate RC's just be lumped into head wire?  
3. How do long lines complicate that (or not)?
4. 


###############################################################################################
Some good SQL:

SELECT count(tile.pkey) as tileKey, tile_type.pkey as tileType, tile_type.name as tileName 
FROM tile INNER JOIN tile_type ON tile.tile_type_pkey=tile_type.pkey
group by tileType 
order by count(tile.pkey)



If wire, which node?
If node, which wire?
Graph theory analog to folding problem

First insight: express as bipartite graph
    - Is this a good formulation?

Give me biggest bicliques (max node cardinality biclique is not quite what we want but is n**2- we want max edge cardinality biclique)

He found paper using monte carlo
    - Found discriminating set 
    - Key param is size of discriminiting set = it is 1 u and 1 v
    - Then it is an mxn scan

Distributing bsc says if disc set size is less than 1 just brute force it - test each row and each column

Once you do this you need to do a set cover 
    - He implemented greedy set cover

3 steps:
    - formulate as bipartite graph
    - find max cardinality edge bicliques w/monte carlo method
    - use greedy set cover to find cover (thinks maybe within 2x)
        - dlx (dancing links) is probably the right way to go
        - but this might not be what we want because bicliques we formulate in step 2 don't lead to exact set cover 
        - exact set cover is where the subsets are disjoint

Steps 1 and 2 will always work
Step 3 may be not very good but could be improved

The linear scan is a problem
    - Each tile has a set of subgraphs which potentially contain the solution
        - Have to scan for it
        - With exact cover could do a lookup 

Is there something that could do steps 2 & 3 in one step?

Steps 2 and 3 are both np complete

Find complete bicliques (set of edge in each bipartite graph which are complete)

Can we exploit structure in a more straightforward manner and formulate it in a different way

- Bicliques subspace clustering (bsc) - On Finding the Maximum Edge Biclique Clustering in a Bipartite Graph
    - There is another paper that says there aren't any good algorithms



In the bip graph u's are tiles, v's are patterns
When we form the complete subgraphs, we have chosen that some tiles don't use a subgraph, some wires don't use a subgraph
    - When you encounter a None

Impedance mismatch between Vivado and VPR

VPR representation:

- In Vivado you have site pins, nodes, and pips
    - Vivado packs to bels

- In VPR you have ipins and opins - very similar to site pins
    - VPR calls sites clusters (equivalent to a site)
    - VPR packs into clusters
    - sources connect to opins
    - sinks connect to ipins
    - when 1-to-1 mapping is clean
    - for LUT inputs (which are all interchangeable), it ties all ipins to a single sink

Mismatch is representation of everything else
    - channels in x and y direction
        - wire segments that run in x and y direction
    - edges which connect all the 6 objects together

Vivado 
    - Elmore delay model = RC + RC + RC
    - Intrinsic delay is just time
    - Time through FET can be modeled as complex RC tree
    - Intrinsic delay is lump sum of the elmore 

- Is RC model that exists between PIPs
- Switch itself is represented by intrinsic delay
- Switch has drive on its output, cap on input (only seen if taken)
- Von calls this internal capacitance - only adds on when enabled
- 7 series fanout loading depends on how many enabled PIPs there are

VPR & Timing Data
- Can add instrinsic delay added to any edge, can have internal cap, output r, ... on edges
- channels can have r and c

Complexity is in 2 places
    - Vivado allows intrinsic delay through site pins
    - ipins don't have intrinsic delay
    - vivado doesn't have rectilinear segments
        - they deccompose wires, build a detailed timing model

Keith has made 1st pass on introducing API
    - he converted array of structs to struct of arrays and created proxy objects to ease transition
    - xifan at U refactored rrgraph as an object (different from what keith did)
        - actively developing it
        - is going to write up a design document
    

VPR focuses on simplified channel wires (x by 4, y by -3)
- they also have "shorts" - pieces of metal that tie objects in the model to one another

VPR doesn't care in PAR about how channels are formed
    - Just cares about downstream edges and timing 

VPR edge traversal operates on channel x and y - is specific to it
    - need to make a narrower interface that hides the detail
    - once that is done, should drop the rr graph
    - rr graph is an artifact of the generator 

VPR needs to decouple from rrgraph
    - Router needs to operate on abstract routing graph: start, stop, eval cost, do prediction, know where it is, where we have been
        - Get rid of channel x and y
    - Need interfaces for router, placer
    - Where can I got, what are edges, what does it cost?

ipin/opin/source/sink can likely stay the same

rectilinear stuff needs to go

1. Who uses the rrgraph and how do they use it?
2. How to hide the details?

Graph exposes ALL details - we need to hide many of them