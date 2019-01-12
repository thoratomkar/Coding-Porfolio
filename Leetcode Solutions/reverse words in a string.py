def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        s = ''
        for i in l:
            s+=i[::-1] + ' '
        return s[:(len(s)-1)]