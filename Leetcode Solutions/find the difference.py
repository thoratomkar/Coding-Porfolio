def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in t:
            if i not in s:
                return i
            elif t.count(i)!=s.count(i):
                return i