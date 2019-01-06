# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 14:24:25 2018

@author: swats
"""

# A Python program to print all  
# permutations of given length 
from itertools import combinations_with_replacement 
from itertools import combinations
from itertools import permutations  
# Get all permutations of length 2 
# and length 2 
mylist = []
perm = permutations([0,1,2,3,4], 2) 
#print(perm) 
# Print the obtained permutations 
sum = 0
for i in list(perm): 
    #print(i)
    for j in i:
    
        sum+=j
    if sum == 4:
        print(i)
    #print(sum)
    sum=0
sum = 0
for i in mylist:
    sum+=i*2
    if sum == 4:
        print(i,i)
    sum=0
    #mylist = []
print('--------------------------------------')
perm1 = combinations_with_replacement([0,1,2,3,4,5,6,7,8], 6) 
        #print(perm) 
        # Print the obtained permutations 
sum = 0
for i in list(perm1): 
    #print(i)
    for j in i:
        sum+=j
    if sum == 48:
        #print('hi')
        final_list=list(i)
        print(final_list)
        s = ''.join(str(e) for e in final_list)
        print(type(s))
        print(s)
        #print(sum)
    sum=0
        #mylist = []