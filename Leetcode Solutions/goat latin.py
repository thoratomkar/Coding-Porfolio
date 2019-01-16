def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = S.split()
        for i in range(len(l)):
            x = l[i]
             
            if x[0].lower() in 'aeiou':
                x = x + 'ma'+'a'*(i+1)
                l[i] = x
            else:
                l1 = list(x)
                temp = l1[0]
                l1[0]=''
                t = ''.join(l1)
                
                x = t + temp + 'ma' + 'a'*(i+1)
                l[i] = x
        
        return ' '.join((l))