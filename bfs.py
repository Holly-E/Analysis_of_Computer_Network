# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import deque to have run time O(1) for append and pop vs O(n) traditional runtime
from collections import deque

def bfs_visited(ugraph, start_node):
    """
    Takes an undirected graph and the start node and returns 
    the set consisting of all nodes that are visited by a bfs 
    originating at start node
    """
    # initialize Q as a queue holding the start node
    queue = deque([start_node])
    visited = {start_node}
    
    while len(queue) != 0:
        current_node = queue.popleft()
        for neighbor in ugraph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return visited
   
#print(bfs_visited({1:[2, 3], 2: [1, 5], 3: [1], 4: [], 5: [2]}, 1))

def cc_visited(ugraph):
    """
    Takes an undirected graph and returns a list of sets, where each set 
    consists of all the nodes (and nothing else) in a connected component, 
    and there is exactly one set in the list for each connected component in
    ugraph and nothing else.
    """
    remaining_nodes = [key for key in ugraph.keys()]
    connected = []
    while remaining_nodes != []:
        node = remaining_nodes[0]
        component = bfs_visited(ugraph, node)
        connected.append(component)
        for connected_node in component:
            remaining_nodes.remove(connected_node)
    return connected

#print(cc_visited({1:[2, 3], 2: [1, 5], 3: [1], 4: [], 5: [2]})) 
    
def largest_cc_size(ugraph):
    """
    Takes undirected graph ugraph and returns the size (integer) of 
    the largest connected component in ugraph.
    """
    