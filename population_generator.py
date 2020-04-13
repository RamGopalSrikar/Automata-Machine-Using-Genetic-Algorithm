#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:28:20 2020

@author: srikarkatakam
"""

import numpy as np
import copy

def population_generator(ind,rule_list,npop):
    
    pop_gen=dict()
    k=len(rule_list)
    for i in range(npop):
        temp=copy.deepcopy(ind)
        for j in range(len(temp['table'])):
            temp['table'][j].append(rule_list[np.random.randint(0,k)])
        
        pop_gen[str(i)]=temp
    
    return pop_gen
        
    