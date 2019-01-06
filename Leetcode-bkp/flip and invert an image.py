def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        l = []
        for i in A:
            #temp = []
            temp = i[::-1]
            #return temp
            for j in range(len(temp)):
                if temp[j]==1:
                    temp[j]=0
                else:
                    temp[j]=1
            #return temp
            l.append(temp)  
        
        return l