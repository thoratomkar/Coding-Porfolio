def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i in d.keys():
                d[i] +=1
            else:
                d[i]=1
        #return d
        
        for i in range(len(s)):
            c = s[i]
            if d[c]==1:
                return i
            
        return -1