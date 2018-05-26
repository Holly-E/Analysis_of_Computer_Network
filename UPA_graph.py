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
import timeit #time.clock() might be prettier: start = time.clock() ... do something ...somelist.append(time.clock() - start)
import matplotlib.pyplot as plt
import gc




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
    Create undirected graph where every new node added randomly connects to a set 
    number of existing nodes.
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
attack_order = func.fast_targeted_order(upa_graph)

upa_y = bfs.compute_resilience(upa_graph, attack_order)
#print(upa_y)
 

def run_time_efficiency(num_new_nodes):
    x = []
    fast_y = []
    slow_y = []
    gc.disable()

    for num_nodes in range(10, 1000, 10):
        x.append(num_nodes)
        graph = upa(num_nodes, num_new_nodes)
        
        start = timeit.default_timer()
        func.fast_targeted_order(graph)
        stop = timeit.default_timer()
        
        fast_y.append(stop - start)
        
        start = timeit.default_timer()
        func.targeted_order(graph)
        stop = timeit.default_timer()
        
        slow_y.append(stop - start)
        
    gc.enable()
    return (x, fast_y, slow_y)

#times = run_time_efficiency(5)
#x = times[0]
#fast_y = times[1]
#slow_y = times[2]

#plt.style.use('default')
#fig = plt.figure(figsize = (9, 5))
#ax1 = fig.add_subplot(1, 1, 1)

#ax1.plot(x, slow_y, label = 'Targeted Order') 
#ax1.plot(x, fast_y, label = 'Fast Targeted Order')
#ax1.legend(loc = 'best')
#ax1.set_title('Desktop Python: Efficiency of Targeted Order Functions', weight=600)
#ax1.set_xlabel('Number of Nodes')
#ax1.set_ylabel('Running Time in Seconds')

#plt.savefig('Images/Efficiency Targeted Order V3', orientation='landscape')
#plt.show()