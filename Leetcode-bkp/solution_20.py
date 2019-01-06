class Solution:
         
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        balanced=True
        index=0
        while balanced==True and index<len(s):
            if s[index] in '{[(':
                stack.append(s[index])
                
            else:
                
                if stack==[]:
                    balanced=False
                    return False
                else:
                    p2=stack.pop()
                    
                    if s[index] == "}" and p2 == "{":
                        return True
                    elif s[index] == ")" and p2 == "(":
                        return True
                    elif s[index] == "]" and p2 == "[":
                        return True
                    else: 
                        balanced=False
                        return False
                        
            index+=1
        
        if stack==[] and balanced==True:
            return True
        else:
            return False
        