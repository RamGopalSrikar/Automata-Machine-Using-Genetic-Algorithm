# -*- coding: utf-8 -*-

import copy
import parent_selection as ps
import crossover as cr
from tabulate import tabulate

def version_one(npop,gen,pop_dict,high_fitness_org,mu,crossover_rate,passes):
    
    pop_gen=copy.deepcopy(pop_dict)
    temp=dict()
    bestsolution=dict()
    high_fitness=copy.deepcopy(high_fitness_org['fitness'])
    best_solution=copy.deepcopy(high_fitness_org)
    print('after initialization')
    display(best_solution,passes)
    avg_fit=[]
    high_fit=[]
    org_gen=copy.deepcopy(gen)
    
    while(gen>0):
        
        gen=gen-1
        popc=dict()
        popp=dict()
        count=0
        count2=npop
        count1=0
        
        
        cdf=[0 for i in range(0,npop)]
        
        m=0
        for it in pop_gen.values():
            cdf[m]=it['fitness']
            m=m+1
            
          
        for j in range(npop//2):
            #parent selection
            p1,p2=ps.exponential_ranking(pop_gen,npop,cdf)
            #child generation
            c1,c2=cr.crossover(p1,p2,mu,crossover_rate,passes)
            
            if(c1['fitness']>high_fitness):
                bestsolution=copy.deepcopy(c1)
                high_fitness=c1['fitness']
                
            if(c2['fitness']>high_fitness):
                bestsolution=copy.deepcopy(c2)
                high_fitness=c2['fitness']
            
            popc[str(count)]=copy.deepcopy(c1)
            popc[str(count+1)]=copy.deepcopy(c2)
            count=count+2
            
            pop_gen[str(count2)]=copy.deepcopy(c1)
            pop_gen[str(count2+1)]=copy.deepcopy(c2)
            count2=count2+2
            
            popp[str(count1)]=copy.deepcopy(p1)
            popp[str(count1+1)]=copy.deepcopy(p2)
            count1=count1+2
        
        pop_ordered=sorted(pop_gen.items(),key=lambda x: x[1]['fitness'])
        
        i=0
        temp.clear()
        
        for item1 in pop_ordered:
            temp[str(i)]=pop_gen[item1[0]]
            i=i+1
            if(i>=npop):
                break
            
       
        pop_gen.clear()
        pop_gen=copy.deepcopy(temp)
        
        avg_fitness=0
        
        for item in pop_gen.values():
            avg_fitness=avg_fitness+item['fitness']
        
        avg_fit.append(avg_fitness/npop)
        high_fit.append(pop_gen[str(0)]['fitness'])
       
        
        
    print('after running GA algorithm')
    display(pop_gen[str(0)],passes)
    return high_fit,avg_fit
            



def display(best_sol,passes):
    print('initial state : {}'.format(best_sol['initial']))
    print('goal state : {}'.format(best_sol['goal']))
    print('finial state :{}  after {} passes'.format(best_sol['final'],passes))
    print('fitness : {}'.format(best_sol['fitness']))
    print()
    print(tabulate(best_sol['table'],['state','rule']))
    



            
