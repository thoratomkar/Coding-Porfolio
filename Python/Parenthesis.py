# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 10:21:25 2018

@author: swats
"""

from Stack import Stack
    
def is_balanced(string):
        s=Stack()
        balanced = True
        index=0
        while balanced and index < len(string):
            paren = string[index] 
            if paren in "{[(":
                s.push(paren)
            else:
                if s.is_empty():
                    balanced = False
                else:
                    top=s.pop()
                    
                    if not is_matched(top,paren):
                        balanced = False
                index +=1
        if s.is_empty() and balanced:
            return True
        else:
            return False
def is_matched(p1,p2):
        if p1 == "{" and p2 == "}":
            return True
        elif p1 == "(" and p2 == ")":
            return True
        elif p1 == "[" and p2 == "]":
            return True
        else: 
            return False
        
print(is_balanced("{[)]}"))

        