def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        l = s.split()
        if len(l)==0:
            return 0
        return len(l[-1])