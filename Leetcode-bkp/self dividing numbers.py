def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l = []
        
        for i in range(left,right+1):
            valid = True
            N=i
            while N >0:                
                x = N%10
                if x==0:
                    valid = False
                    break
                if i%x != 0:
                    valid = False
                    break
                else:
                    #sumi = sumi*10 + x
                    N= N//10
            if valid == True:
                l.append(i)
        return l