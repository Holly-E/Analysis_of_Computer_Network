# -*- coding: utf-8 -*-
"""
These functions will allow us to determine how much an attack on a node that destroys the node and its edges will affect the largest connected components of a graph.
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
    connected = cc_visited(ugraph)
    largest = 0
    for component in connected:
        if len(component) > largest:
            largest = len(component)
            
    return largest

#print(largest_cc_size({1:[2, 3], 2: [1, 5], 3: [1], 4: [], 5: [2]})) 
    
def compute_resilience(ugraph, attack_order):
    """ 
    Takes undirected graph ugraph, and a list of nodes simulating servers: 
    attack_order. For each attacked node, the given node and its edges are removed 
    from the graph. Then computes the size of the largest connected component 
    for the resulting graph. Returns a list whose k+1th entry is the size of 
    the largest connected component in the graph after the removal of the 
    first k nodes. The first entry is the size of the largest connected 
    component in the original graph.
    """
    resilience = [largest_cc_size(ugraph)]
    for node in attack_order:
        ugraph.pop(node)
        for _dummy_key, value in ugraph.items():
            if node in value:
                value.remove(node)
        resilience.append(largest_cc_size(ugraph))

    return resilience  

#print(compute_resilience({1:[2, 3], 2: [1, 5], 3: [1], 4: [], 5: [2]}, [2, 5])) 