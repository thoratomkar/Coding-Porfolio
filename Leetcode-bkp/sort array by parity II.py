def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        
        odd =[]
        even = []
        
        for i in range(len(A)):
            if A[i]%2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        res = []
        for i in range(len(odd)):
            res.append(even[i])
            res.append(odd[i])
        
        return res
        """
        
        res = [0]*len(A)
        odd = 1
        even = 0
        
        for i in A:
            if i%2 == 0:
                res[even] = i
                even +=2
            else:
                res[odd] = i
                odd +=2
                
        return res