def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        l = list(magazine)
        s = list(ransomNote)
        for i in ransomNote:
            if i not in l:
                return False
            else:
                del l[l.index(i)]
                del s[s.index(i)]
        if s == []:
            return True
        return False