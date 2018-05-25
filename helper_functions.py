#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:08:31 2018

@author: hollyerickson
functions on graphs: copy, delete_node, targeted_order, num_edges, random_order
"""
from random import shuffle

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order


def num_edges(ugraph):
    """
    calculate number of edges, divide by two since graph is undirected
    """
    edges = 0
    for key in ugraph:
        edges += len(ugraph[key])
    return edges / 2


def random_order(graph):
    """
    takes a graph and returns a list of the nodes in the graph in some random order
    """
    key_list = []
    for key in graph:
        key_list.append(key)
    # random.shuffle happens in place on the list and returns nothing
    shuffle(key_list)
    return key_list
