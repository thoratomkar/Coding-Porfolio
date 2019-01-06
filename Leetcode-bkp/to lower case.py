def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        upper_to_lower = ord('a') - ord('A') 
        s = []
        for ch in str:            
            if 'A' <= ch <= 'Z':
                s.append(chr(ord(ch) + upper_to_lower))
            else:
                s.append(ch)
        return "".join(s)