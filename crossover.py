# -*- coding: utf-8 -*-
import numpy as np
import copy
import fitnessEval as fit
import finalState as fs
import mutate
def crossover(p1,p2,mu,crossover_rate,passes):
    c1=copy.deepcopy(p1)
    c2=copy.deepcopy(p2)
   
    
#    alpha=0.3
    
    count=0
    for list1,list2 in zip(p1['table'],p2['table']):
        if(np.random.uniform(0,1)<=crossover_rate):
            c1['table'][count][1]=list2[1]
            c2['table'][count][1]=list1[1]
        count=count+1
        

    
    c1m=mutate.mutate(c1,mu)
    c2m=mutate.mutate(c2,mu)
    
    fs.finalState(c1m,passes)
    fit.calculate_fitness(c1m)
    
    fs.finalState(c2m,passes)
    fit.calculate_fitness(c2m)
    
    return c1m,c2m


def crossover_onepoint(p1,p2,mu,crossover_rate,passes):
    c1=copy.deepcopy(p1)
    c2=copy.deepcopy(p2)
   
    
#    alpha=0.3
    
    count=0
    point=np.random.randint(0,32)
    for list1,list2 in zip(p1['table'],p2['table']):
        if(count>=point):
            c1['table'][count][1]=list2[1]
            c2['table'][count][1]=list1[1]
        count=count+1
        if(count>=32):
            break

    
    c1m=mutate.mutate(c1,mu)
    c2m=mutate.mutate(c2,mu)
    
    fs.finalState(c1m,passes)
    fit.calculate_fitness(c1m)
    
    fs.finalState(c1m,passes)
    fit.calculate_fitness(c1m)
    
    return c1m,c2m