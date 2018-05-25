#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 15:44:39 2018

@author: hollyerickson
Code for loading the resilience comparison graph.
"""
import matplotlib.pyplot as plt

from Computer_network_simulation import network_y
from ER_undirected_graphV2 import er_y
from UPA_graph import upa_y

#plt.style.use('seaborn-whitegrid')
fig = plt.figure(figsize = (9, 5))
ax1 = fig.add_subplot(1, 1, 1)

x = [num for num in range(0, 1240)]

ax1.plot(x, network_y, 'red', label='Computer network sim')
ax1.plot(x, er_y, 'blue', label='ER graph, p = 0.00397')
ax1.plot(x, upa_y, 'green', label='UPA graph, m = 3')

ax1.set_title('Resilience Comparison - Random Attack', weight=600)
ax1.set_xlabel('Number of Nodes Removed')
ax1.set_ylabel('Size of Largest Connect Component')
plt.legend(loc='best')

#plt.savefig('Images/Resilience Comparison', orientation='landscape')
#plt.show()

