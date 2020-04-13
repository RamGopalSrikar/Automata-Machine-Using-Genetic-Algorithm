# -*- coding: utf-8 -*-
import numpy as np
import copy

def mutate(C,mu):
    Cm=copy.deepcopy(C)
    count=0
    for list1 in C['table']:
        if(np.random.uniform(0,1)<=mu):
            Cm['table'][count][1]=np.random.randint(0,4)
        count=count+1
    return Cm
