# -*- coding: utf-8 -*-

#NAME : RAM GOPAL SRIKAR
#STUDENT ID: 40106010
import population_generator as pop
import table_generator as tab
import finalState as fs
import numpy as np
import fitnessEval as fit
import version_one as one
import statistics as st
import matplotlib.pyplot as plt



#function setting
def adjust_len(s,l=8):
    diff=8-len(s)
    if(diff>0):
        for i in range(0,diff):
            s='0'+s
    return s

#paramter setting
npop=300
gen=100
mu=0.1
crossover_rate=0.4
runs=20

#version_2


mu2=0.2
crossover_rate2=0.4


#problem paramter
rule_list=[0,1,2,3]
window_bits=5
total_bits=8

best_fitness1=[]
avg_fitness1=[]
mean_bestfit1=[]
stddev_bestfit1=[]
mean_avgfit1=[]
stddev_avgfit1=[] 


for k in range(runs):
    np.random.seed(100*(k))
    passes=np.random.randint(1,10)
    print(passes)
    print('passes {}'.format(passes))
    initial_bits=adjust_len("{0:b}".format(np.random.randint(0,256)),total_bits)
    goal_bits=adjust_len("{0:b}".format(np.random.randint(0,256)),total_bits)
    while np.array_equal(initial_bits, goal_bits):
         goal_bits = adjust_len("{0:b}".format(np.random.randint(0,256)),total_bits)
    print('run {}'.format(k))
    #population generation
    ind=tab.table_generator(initial_bits,goal_bits,window_bits)
    
    pop_gen=pop.population_generator(ind,rule_list,npop)
    high_fitness=0
    for i in range(npop):
        fs.finalState(pop_gen[str(i)],passes)
        fit.calculate_fitness(pop_gen[str(i)])
        if(pop_gen[str(i)]['fitness']>high_fitness):
            high_fitness_org=pop_gen[str(i)]
            high_fitness=pop_gen[str(i)]['fitness']
    #version one
    
    best,avg=one.version_one(npop,gen,pop_gen,high_fitness_org,mu,crossover_rate,passes)
    best_fitness1.append(best)
    avg_fitness1.append(avg)
    
    
  
for i in range(0,gen):
    x1=np.asarray(best_fitness1)
    y1=np.asarray(avg_fitness1)
    mean_bestfit1.append(st.mean(x1[:,i]))
    stddev_bestfit1.append(st.stdev(x1[:,i]))
    
    mean_avgfit1.append(st.mean(y1[:,i]))
    stddev_avgfit1.append(st.stdev(y1[:,i]))

plt.plot(mean_bestfit1,'r--')
plt.xlim(0,gen)
plt.xlabel('generations')
plt.ylabel('mean')
plt.title('(GA) 1 versions mean of maximum fitness')
plt.grid(True)
plt.legend()
plt.show()     

plt.plot(stddev_bestfit1,'r--')
plt.xlim(0,gen)
plt.xlabel('generations')
plt.ylabel('standered deviation')
plt.title('(GA) 1 versions  standered deviation of maximum  fitness')
plt.grid(True)
plt.legend()
plt.show()  

plt.plot(mean_avgfit1,'r--')
plt.xlim(0,gen)
plt.xlabel('generations')
plt.ylabel('mean')
plt.title('(GA) 1 versions  mean of average fitness')
plt.grid(True)
plt.legend()
plt.show()     

plt.plot(stddev_avgfit1,'r--')
plt.xlim(0,gen)
plt.xlabel('generations')
plt.ylabel('standered deviation')
plt.title('(GA) 1 versions standered deviations of average fitness')
plt.grid(True)
plt.legend()
    
    
    
    
    
    
    

