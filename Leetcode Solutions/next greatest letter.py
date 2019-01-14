def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        
        l = []
        for i in letters:
            if i != target and (ord(i)-ord(target))>0:
                l.append((ord(i)-ord(target)))
            else:
                l.append(99999)
        
        return letters[l.index(min(l))]
            
        """
        for letter in letters:
            if letter > target:
                return letter
        return letters[0] # If not found