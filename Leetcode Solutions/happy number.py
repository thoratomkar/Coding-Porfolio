def isHappy(self, n):
        """
        :type n: int
        :rtype: bool        
        """        
        seen = set()
        
        while n!=1:
            add = 0
            for i in str(n):
                add += int(i)**2
            n = add            
            if n not in seen:
                seen.add(n)
            else:
                return False
        return True