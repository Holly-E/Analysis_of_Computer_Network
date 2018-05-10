#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:18:27 2018

@author: hollyerickson

Graph where for every ordered pair of distinct nodes (i,j), the modified algorithm adds the UNDIRECTED edge from i to j with probability p.
"""
import random
#from collections import defaultdict

def er(num_nodes, prob):
    g = {}
    for num in range(num_nodes):
        g[num] = []
    nodes = [num for num in range(num_nodes)]
    num_edges = prob *  num_nodes
    
    for num in range(num_nodes):
        #random.shuffle(nodes)
        edges = 0
        edge_list = []
        while edges < num_edges:
            edge = random.choice(nodes)
            if edge != num:
                edge_list.append(edge)
                g[edge].append(num)
            edges += 1
        g[num].extend(edge_list)
    
    for key, val in g.items():
        g[key] = set(val)
        
    return g
    
#print(er(10, 0.5))