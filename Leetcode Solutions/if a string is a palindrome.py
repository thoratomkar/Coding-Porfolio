def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        
        x = s.lower()
        s_final = ""
        l = []
        for i in x:
            if i.isalpha() or i.isdigit():
                s_final += i
                l.append(i)
        
        return s_final == s_final[::-1]
        """        
        
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]