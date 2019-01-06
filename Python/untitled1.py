# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:57:50 2018

@author: swats
"""
'''
def missingWords(s, t):
    slist = []
    slist = s.split()
    tlist = []
    tlist = t.split()
   
    
    if tlist == "" or slist == "":
        return slist
        
    
    for x in tlist:
        
        for y in range(0, len(slist)):
            
            if x == slist[y]:
                slist.pop(y)
                break
            
                
    return slist

print(missingWords('123, omkar','omkar'))
'''
def findSubstrings(s):
    temp = s
    newlist = []
    vowels = ['a','e','i','o','u']
    for i in s:
        t = s.index(i)
        if i in vowels:
            for j in s[::-1]:
                u = s.index(j)
                if j not in vowels:
                    x = s[t:u+1]
                    newlist.append(x)
                    for k in range(1,len(x)):
                        print(x)
                        x.replace(x[k],"")
                        print(x)
                        findSubstrings(x)
    print(newlist)
    
findSubstrings('abc')