def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        
        e = []
        o = []
        for i in A:
            if i%2 == 0:
                e.append(i)
            else:
                o.append(i)
        
        return e + o
        """
        
        i = 0
        j = len(A) -1
        while i < j:
            if A[i]%2 > A[j]%2:
                A[i],A[j] = A[j],A[i]
                
            if A[i]%2 == 0:
                i+=1
            if A[j]%2 == 1:
                j-=1
        return A