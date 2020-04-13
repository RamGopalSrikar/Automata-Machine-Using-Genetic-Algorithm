# -*- coding: utf-8 -*-


def table_generator(initial_state,goal_state,bits):
    ind_dict=dict()
    ind_dict['initial']=initial_state
    ind_dict['goal']=goal_state

    list_table=[]
    no=2**bits
    
    for i in range(no):
        s="{0:b}".format(i)
        if(len(s)<bits):
            for j in range(bits-len(s)):
                s='0'+s
        list_table.append([s])
        
    ind_dict['table']=list_table
    
    return ind_dict



        