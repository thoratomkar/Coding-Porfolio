def hammingDistance(x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        
        x_bin = list('{0:032b}'.format(x))
        y_bin = list('{0:032b}'.format(y))
        
        count = 0
        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                count +=1
            
        return count
        """

        return bin (x^y).count('1')