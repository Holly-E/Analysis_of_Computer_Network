#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:18:27 2018

@author: hollyerickson

Create the UPA (Undirected vs Differential Power Analysis) graph.
"""

import alg_upa_trial as alg
import helper_functions as func
import bfs

def make_complete_graph(num_nodes):
    '''
    Parameter #nodes and returns a dictionary corresponding to 
    a complete directed graph with the specified number of nodes.
    It contains all possible edges, self-loops are not allowed. 
    The nodes of the graph should be numbered 0 to num_nodes - 1.
    '''
    
    if num_nodes <= 0:
        return {}
    
    new_dict = {}
    for num in range(num_nodes):
        neighbors = []
        for neighbor in range(num_nodes):
            if neighbor != num:
                neighbors.append(neighbor)
        new_dict[num] = set(neighbors)
    return new_dict

def upa(num_nodes, num_new_nodes):
    """
    Create undirected graph where every new node added randomly connects to a set number of existing nodes.
    """
    upa_graph = make_complete_graph(num_new_nodes)
    graph = alg.UPATrial(num_new_nodes)
    for num in range(num_new_nodes, num_nodes):
        new_node_neighbors = graph.run_trial(num_new_nodes)
        upa_graph[num] = new_node_neighbors
        # make graph undirected
        for neighbor in new_node_neighbors:
            upa_graph[neighbor].add(num)
    
    return upa_graph

 #1239 nodes and approx 3047 edges for comp network sim
# 3047 / 1239 = approx 2.459 edges per node
 
upa_graph = upa(1239, 3)
#print (func.num_edges(upa_graph))
attack_order = func.random_order(upa_graph)

upa_y = bfs.compute_resilience(upa_graph, attack_order)
#print(upa_y)