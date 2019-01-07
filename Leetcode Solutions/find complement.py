def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=""
        x = bin(num)
        x = x[2:]
        
        for i in x:
            if i=='1':
                s +='0'
            else:
                s +='1'
        return int(s,2)