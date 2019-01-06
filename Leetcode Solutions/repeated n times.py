def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = {}
        
        for i in range(len(A)):
            if A[i] in d.keys():
                return A[i]
            else:
                d[A[i]] = 1