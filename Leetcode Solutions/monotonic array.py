def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag_inc = False
        flag_dec = False
        if len(A) <3:
            return True
        
        for i in range(1,len(A)):
            if A[i-1]< A[i]:
                flag_inc = True
            if A[i-1]> A[i]:
                flag_dec = True
            if flag_inc and flag_dec:
                return False
        
        return True