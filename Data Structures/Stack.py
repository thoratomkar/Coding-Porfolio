# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 10:08:43 2018

@author: swats
"""

class Stack():
    def __init__(self):
        self.items=[]
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        self.items.pop()
    
    #top of the stack
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return self.items == []
    
    def display(self):
        return self.items
    
s=Stack()
'''
#print(s.is_empty())
s.push("A")
s.push("B")
s.push("C")
s.push("D")
'''
#print(s.display())
#print(s.is_empty())
#print(s.peek())
#s.pop()
#print(s.display())
#print(s.peek())
