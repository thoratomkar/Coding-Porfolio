def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s=''
        
        l = []
        while N>0:
            
            x = N%2
            s += str(x)
            N = N//2
        s = s[::-1]
        
        for i in range(0,len(s)):
            
            if s[i]=='1':
                l.append(i)
        
        m=0
        for i in range(0,len(l)-1):
            d = abs(l[i]-l[i+1])
            
            if d>m:
                m=d
        return m
        