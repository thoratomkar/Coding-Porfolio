def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in string.ascii_lowercase:
            if s.count(i) != t.count(i):
                return False
        return True