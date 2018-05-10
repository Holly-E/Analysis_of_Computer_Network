#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:18:27 2018

@author: hollyerickson

Create the UPA (Undirected vs Differential Power Analysis) graph.
"""

import alg_upa_trial as alg


def upa(num_nodes, num_new_nodes):
    """
    Create undirected graph where every new node added randomly connects to a set number of existing nodes.
    """
    upa_graph = ind.make_complete_graph(num_new_nodes)
    graph = alg.UPATrial(num_new_nodes)
    for num in range(num_new_nodes, num_nodes):
        new_node_neighbors = graph.run_trial(num_new_nodes)
        upa_graph[num] = new_node_neighbors
    return upa_graph

 
upa_graph = upa(27770, 13)
