def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        
        flag = True
        x = bin(n)
        #print(x)
        for i in range(3,len(x)):
            if x[i-1]==x[i]:
                return False
        return flag
        """
        s = bin(n)
        return '00' not in s and '11' not in s