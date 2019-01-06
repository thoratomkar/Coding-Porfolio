def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def dictionary(l,d):
            
            j = 0
            for i in range(ord('a'), ord('z') + 1):                
                d[chr(i)] = l[j]
                #print(j)
                j+=1
            
            
        d = {}
        dictionary([".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."],d)
        l = []
        for i in words:
            s = []
            for j in i:
                s.append(d.get(j))
            
            l.append("".join(s))
            
        return len(set(l))