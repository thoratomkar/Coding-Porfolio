# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 09:49:20 2018

@author: swats
"""

class Stack():
    def __init__(self):
        self.items=[]
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        self.items.pop()
    
    def minimum(self):
        index=0
        minimum=9999999
        while index <len(self.items):
            if self.items[index]<minimum:
                minimum=self.items[index]
                index+=1
            else:
                index+=1
        return minimum
    

s=Stack()

s.push(4)
s.push(3)
s.push(2)
s.push(1)

print(s.minimum())