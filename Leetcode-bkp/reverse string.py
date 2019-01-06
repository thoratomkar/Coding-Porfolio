def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = ''
        i = len(s)-1
        while i>=0:
            l += s[i]
            i -=1
        return l