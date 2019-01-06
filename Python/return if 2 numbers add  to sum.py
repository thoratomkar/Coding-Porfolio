# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 00:25:14 2018

@author: swats
"""

def check_sum(l,k):
    if l == []:
        return 'Empty'
    else:
        for i in range(0,len(l)):
            for j in range(i+1,len(l)):
                #print('here')
                if l[i] + l[j] == k:
                    #count+=1
                    return True
        return False
        

l = [10,15,3,7]
k =11
print(check_sum(l,k))