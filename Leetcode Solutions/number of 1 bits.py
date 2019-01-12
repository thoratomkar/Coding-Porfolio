def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = '{0:032b}'.format(n)
        #b = bin(n)
        count =0
        for i in binary:
            if i=='1':
                count+=1
        return count