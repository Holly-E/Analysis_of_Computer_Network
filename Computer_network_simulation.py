#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:30:15 2018

@author: hollyerickson

Code for loading example computer network.
"""


# general imports
#import urllib2 #urllib2 not available in Python3
from urllib.request import urlopen


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"
import bfs

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urlopen(graph_url)
    graph_text = graph_file.read().decode("utf-8")
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print ("Loaded graph with", len(graph_lines), "nodes")
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

citation_graph = load_graph(CITATION_URL)
    
#print(bfs.compute_resilience(citation_graph, [1346, 1129, 52])) 
