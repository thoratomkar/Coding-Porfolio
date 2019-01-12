def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        final = (A+" "+B).split(" ")
        result = []
        for i in final:
            if final.count(i) == 1:
                result.append(i)
        return result
                