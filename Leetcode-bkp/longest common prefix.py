def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        x = min(strs, key=len)
        if x == "":
            return ""
        count = 0
        for i in (strs):          
                
            while x !="":
                if x not in  i:
                    x = x[:len(x)-1]
                else:
                    if x!=i[:len(x)]:
                        x = x[:len(x)-1]
                        
                    else:
                        count+=1
                        break
        if count == len(strs):
            return x
        return ""