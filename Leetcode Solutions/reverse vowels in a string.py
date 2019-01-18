def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        v = []
        
        for i in range(len(l)):
            if l[i].lower() in 'aeiou':
                v.append(l[i])
                l[i] = '*'
        
        j = len(v)-1
        for i in range(len(l)):
            if l[i]=='*':
                l[i] = v[j]
                j-=1
        
        return ''.join(l)
                