def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        
        S1 = list(S)
        S = list(S)
        #S1 = list(S)
        l = []
        res = []
        
        for i in range(len(S1)):
            if S1[i] == C:
                l.append(i)
                S1[i] = 0
        for i in range(len(S)):
            #index = S.index(i)
            mini=9999
            for j in l:
                mini = min(abs(i - j),mini)
            res.append(mini)
        return res            
        """
        
        res = []
        l =[]
        for i,v in enumerate(S):
            if v==C:
                l.append(i)
        
        for i in range(len(S)):
            mini = 9999
            for j in l:
                mini = (min(abs(i-j),mini))
            res.append(mini)
        return res