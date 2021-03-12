# Notes on litghost's database representation

# Example using CLK_PMV (only has 1 tile)
- Tile type 13 is CLK_PMV
- There is one tile of type 13, it is 9243
- Looking in the wire_in_tile table, there are 1664 wires in a type 13 tile (CLK_PMV)
    - These wire_in_tile pkey of 7514 through 9177
- Looking in the node table, there are 248 nodes in tile 9423
    - ? Do these 248 nodes start in tile 9423 or just pass through it in some way?
    - They are nodes 2250534 through 2251257
    - They have wire_in_tile_pkey values of 8518 through 8721
- Looking in the wire table
    - node_pkey 2250534 shows it is in tile 9243 and is wire_in_tile_pkey 7514 and is wire 7328465

To find the pips a node can drive (2251091):
1. The node table tells you it is tile 9243 and wire_in_tile_pkey 8379
2. Looking in wire table for 2251091 gives 2 wires:
    - wire 7329975(8379) in tile 9243
    - wire 7329974(73944) in tile 12166
3. For the 2nd one, looking in wire_in_tile tells us it is in tile type 97, is called INT_INTERFACE_LOGIC_OUTS_B1 and drives a PIP
4. Looking in wire table, wire 7329974 shows it is in tile 12166, is wire in tile 73944, and is node 2251091

# Queries:
1. I am a wire, what node am I part of?
    - Look in wire table using wire #
        - Will give tile #, node #, wit #
2. I am a wire, what are all the other wires I am shorted to?
    - Do #1 to get node #
    - Look in wire table using node #
        - Will return multiple rows - all wire #'s, along with their wit #'s and tile #'s
3. I am a wire, what is my tile's X/Y coord?
    - Look in wire table using wire #
        - Will give tile #
    - Look in tile table using tile #
        - Will give x,y
2. I am a wire, what are locations of wires I am shorted to?
    - Do #2 to get list of other wires in my node.  
    - Then, for each:
        - Do #3 to get X/Y coord of that wire
4. I am a node, what wires are part of me?
    - Look in wire table using node #
        - Will return multiple rows containing wire #'s, along with their wit #'s and tile #'s
5. I am a node, what is my start wit?
    - Look in node table using node # 
        - Will give wit # and tile #
6. I am a node, what is my start wire?
    - Do #5 to get wit # and tile #
    - Look in wire table using node # 
        - Will return multiple rows, each with wire #, wit #, tile #
        - From those rows, select either the one with the matching wit # or tile # 
            - Either one will work
            - Wire # from that row is what you want
    - Look in wire table using wit # and tile #
        - Will give physical wire #
7. What are the PIPs a node can drive?
    - Look in wire table using node # 
        - Will return a bunch of rows, one for each wire #/wit #/tile #
        - For each one, look in wire_in_tile based on aand it will tell
8. If I am a wit, what node am I part of?
    - Must first know tile # or cannot look up
        - Look wire table using wit # and tile #
            - Will give node #

# Graph Folding
- Problem with above is wire table is so huge
- But:
    - May have tiles that share ALL of the same nodes
        - For those tiles, they could all share a common *template* 
        - If there were 1000 such tiles, size reduction would be 1000x
    - More likely, there will be tiles that share SOME of the same nodes
        - Still could use common template for the nodes they have in common
        - Example, maybe all the INT_L tiles interior ot the array have one set of nodes
            - And INT_L tile on the top edge have 90% of the same patterns as them but 10% that only top tiles have
            - They could share the 90%