def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        
        count = 0
        
        
        flag = False
        if word[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            flag = True
        for i in word:
            if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                count +=1
        
        if count == 0 or count == len(word):
            return True
        elif (count == 1 and flag == True):
            return True
        return False
        """
        if word.lower()==word or word.upper()==word:
            return True
        elif word[0].lower()!=word[0] and word[1:].lower()==word[1:]:
            return True
        else:
            return False