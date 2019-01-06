# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 12:58:32 2018

@author: swats
"""

class Queue():
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    
    def push(self,item):
        self.stack1.append(item)
    
    def display(self):
        if self.stack1!=[] and self.stack2==[]:
            return self.stack1
        return self.stack2
    
    def pop(self):
        if self.stack1==[]:
            return 'No element in queue'
        else:
            while self.stack1 !=[]:
                self.stack2.append(self.stack1.pop())
            
        return self.stack2.pop()
    
    def search(self,x):
        while self.stack1!=[] or self.stack2!=[]:
            if x in self.stack1 or x in self.stack2:
                
                return  {self.stack2.index(x)}
            else:
                return 'element not found'
            
    
        
q=Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
print(q.display())
print(q.pop())
print(q.search(3))
print(q.display())        