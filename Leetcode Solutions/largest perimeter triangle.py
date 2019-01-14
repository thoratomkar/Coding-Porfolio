def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        p = 0
        
        x = sorted(A)
        x = x[::-1]

        for i in range(len(x) - 2): 
            if x[i] < (x[i + 1] + x[i + 2]): 
                p = max(p, x[i] + x[i + 1] + x[i + 2]) 
                break
        return p