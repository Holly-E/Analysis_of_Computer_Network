#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:18:27 2018

@author: hollyerickson

"""
import random
import itertools as iter
import helper_functions as func
import bfs

#from collections import defaultdict

def er(num_nodes, prob):
    """
    for every ordered pair of distinct nodes (i,j), the modified algorithm adds the UNDIRECTED 
    edge from i to j with probability p
    """
    er_graph = {}
    for num in range(num_nodes):
        er_graph[num] = set()
    
    # check out itertools to get methods for creating combinations & permutations
    combo_list = list(iter.combinations(range(num_nodes), 2))
    for combo in combo_list:
        # random.random() generates a number between 0 & 1
        rand = random.random()
        if rand < prob:
            er_graph[combo[0]].add(combo[1])
            er_graph[combo[1]].add(combo[0])
    return er_graph
    
er_graph = er(1239, 0.00397)

# 1239 nodes and need approx 3047 edges for comp network sim. What prob provides this expected val?
#Expected val when probability doesn't change:
#  .5(k-1)(k) * p = expected val
# .5 * 1238 * 1239 * p = exp
# exp / 766941 = p
# exp = num edges 
# print( 3047 / 766941 )
# will use .00397 as prob

attack_order = func.random_order(er_graph)
er_y = bfs.compute_resilience(er_graph, attack_order)
#print(er_y)
