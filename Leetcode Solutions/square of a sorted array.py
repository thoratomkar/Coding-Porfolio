def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l = []        
        for i in A:            
            l.append(i**2)        
        l.sort()
        return l