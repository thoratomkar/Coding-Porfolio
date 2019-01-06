# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:05:29 2018

@author: swats
"""

def binary(num):
    bits=[]
    string=""
    if num == 0 or num == 1:
        return num
    else:
        while(num > 0):
           # temp=num
            r=num%2
            bits.append(r)
            num=num//2
        for i in range(bits)
            string+=str(bits.pop())
            return string
    

num=int(input(print ('Enter an integer')))
print(binary(num))