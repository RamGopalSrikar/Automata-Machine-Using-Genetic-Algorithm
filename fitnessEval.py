# -*- coding: utf-8 -*-

import numpy as np

def fitnessEval(ind_table):
    final_state=ind_table['final']
    goal_state=ind_table['goal']
    med=0
    
    for i,j in zip(final_state,goal_state):
        if(i!=j):
            med=med+1
     

    ind_table['fitness']=((8-med)/8)*100
    if "fitness" in ind_table:
        ind_table['fitness']=((8-med)/8)*100
    else:
        ind_table.update({'fitness': ((8-med)/8)*100})        

def calculate_fitness(ind_table):
    final_state=ind_table['final']
    goal_state=ind_table['goal']
    
    fitness_table = np.zeros((len(final_state) + 1 , len(goal_state) + 1), dtype=int)

    for row in range(len(final_state)+1):
        fitness_table[row][0] = row
    for col in range(len(goal_state)+1):
        fitness_table[0][col] = col
    
    for row in range(len(final_state)+1):
        for col in range(len(goal_state)+1):
            if row != 0 and col != 0:  
                if final_state[row-1] == goal_state[col-1]:
                    fitness_table[row][col] = fitness_table[row-1][col-1]
                else:
                    fitness_table[row][col] = min(fitness_table[row-1][col] + 1,
                                          fitness_table[row][col-1] + 1,
                                          fitness_table[row-1][col-1] + 2)
    
    if "fitness" in ind_table:
        ind_table['fitness']=fitness_table[len(final_state)][len(goal_state)]
    else:
        ind_table.update({'fitness': fitness_table[len(final_state)][len(goal_state)]})        

