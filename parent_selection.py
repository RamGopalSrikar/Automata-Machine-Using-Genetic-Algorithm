import numpy as np
import copy

def rand_parentsel(pop_gen,npop):
     q=np.random.permutation(npop)
     p1=pop_gen[str(q[0])]
     p2=pop_gen[str(q[1])]
     return p1,p2
 
def fitness_prob(pop_gen,npop,cost_prob):
    m=np.random.uniform(0,1)
    n=np.random.uniform(0,1)
    
    for i in range(npop):
        if m<=cost_prob[i]:
            p1=pop_gen[str(i)]
            break
    for j in range(npop):    
        if n<=cost_prob[j]:
            p2=pop_gen[str(j)]
            break   
    return p1,p2 
    

def rand_fitness_prob(pop_gen,npop,cost_prob):
    r=np.random.unifrom(0,1)
    if r<0.5:
        q=np.random.permutation(npop)
        p1=pop_gen[q[0]]
        p2=pop_gen[q[1]]
    else:
        m=np.random.uniform(0,1)
        n=np.random.uniform(0,1)
        for i in range(npop):
            if m<=cost_prob[i]:
                p1=pop_gen[i]
                break
        for j in range(npop):    
            if n<=cost_prob[j]:
                p2=pop_gen[j]
                break
    return p1,p2  

def tournament_sel(pop_gen,npop,k=10):
    q1=np.random.permutation(npop)
    q2=np.random.permutation(npop)
    p1_arr=q1[0:k]
    p2_arr=q2[0:k]
    best_costp1=0
    best_costp2=0
    for i in range(k):
        if pop_gen[str(p1_arr[i])]['fitness']>best_costp1:
            temp_p1=pop_gen[str(p1_arr[i])]
            best_costp1=pop_gen[str(p1_arr[i])]['fitness']
        if pop_gen[str(p2_arr[i])]['fitness']>best_costp2:
            temp_p2=pop_gen[str(p2_arr[i])]
            best_costp2=pop_gen[str(p2_arr[i])]['fitness']
    
    p1=copy.deepcopy(temp_p1)
    p2=copy.deepcopy(temp_p2)
    return p1,p2

def rand_tournamet_fitness(pop_gen,npop,cost_prob,k):
    r=np.random.uniform(0,1)
    if r<0.5:
        p1,p2=tournament_sel(pop_gen,npop)
    else:
        p1,p2=fitness_prob(pop_gen,npop,cost_prob)
    return p1,p2
    
def exponential_ranking(pop_gen,npop,fitness):
    sort_cdf=list(sorted(set(fitness),reverse=True))
    
    C=npop-((np.exp(-npop)-1)/(np.exp(-1)-1))
    ranking=[0 for i in range(0,npop)]
    prob=[0 for i in range(0,npop)]
    count=0
    for i in range(len(sort_cdf)):
        for j in range(npop):
            if(sort_cdf[i]==pop_gen[str(j)]['fitness']):
                ranking[j]=count
                count=count+1
    
    for m in range(npop):
        if(m>0):
            prob[m]=prob[m-1]+(1-np.exp(-ranking[m]))/C
        else:
            prob[m]=(1-np.exp(-ranking[m]))/C
            m=m+1
                     
    m=np.random.uniform(0,1)
    n=np.random.uniform(0,1)
    for i in range(npop):
        if m<=prob[i]:
            p1=pop_gen[str(i)]
            break
    for j in range(npop):    
        if n<=prob[j]:
            p2=pop_gen[str(j)]
            break
    return p1,p2  
   