def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l=[]
        
        for i in range(1,numRows+1):
            t = [1]*i
            for j in range (1,i-1):
                t[j] = l[i-2][j-1] + l[i-2][j]
            l.append(t)
        
        return l