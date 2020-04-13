# -*- coding: utf-8 -*-

import copy


def finalState(ind_table,passes):
    temp=copy.deepcopy(ind_table)
    initial_state=temp['initial']
    goal_state=temp['goal']
    table=temp['table']
    l=len(initial_state)
    w=len(temp['table'][0][0])
    
    current_state=initial_state
    next_state=copy.deepcopy(initial_state)
    for i in range(passes):
        for j in range(l):
            if(j+w<l):
                sub=current_state[j:j+w]
            else:
                k=len(current_state[j:-1]+current_state[-1])
                sub=current_state[j:-1]+current_state[-1]+current_state[0:w-k]
            
            for list1 in table:
                if(list1[0]==sub):
                    rule=list1[1]
                    break
            
            if(rule==0):
                str_opr='0'
            elif(rule==1):
                str_opr='1'
            elif(rule==2):
                str_opr='_'
            elif(rule==3):
                str_opr=sub[2]
            else:
                print('no valid rule')
                
            if(rule==3):
                if(j+round(w/2)-1<l):
                    next_state=next_state[0:j+round(w/2)-1]+str_opr+next_state[j+round(w/2):l]
                else:
                    l1=j+round(w/2)-l-1
                    next_state=next_state[0:l1+1]+str_opr+next_state[l1:-1]+next_state[-1]
            else:    
                if(j+round(w/2)<l):
                    next_state=next_state[0:j+round(w/2)]+str_opr+next_state[j+round(w/2)+1:l]
                else:
                    l1=j+round(w/2)-l
                    next_state=next_state[0:l1]+str_opr+next_state[l1+1:-1]+next_state[-1]
                
        current_state=copy.deepcopy(next_state)
        if(current_state==goal_state):
            break
    
    if "final" in ind_table:
        ind_table['final']=current_state
    else:
        ind_table.update({'final': current_state}) 
    