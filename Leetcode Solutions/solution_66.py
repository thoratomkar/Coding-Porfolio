class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        List = []
        total = 0
        l = len(digits)
        for i in range(0,l):
            #x=digits.pop()
            total = total + digits[i]*(10)**(l-i-1)
        total+=1
        
        while total > 0:
            t=total
            total = total//10
            n=t%10
            List.append(n)
            
        
            
        return List[::-1]