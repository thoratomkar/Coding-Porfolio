def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left = right = 0
        res = [0]
        for i in S:
            if i == "I":
                right += 1
                res.append(right)
            else:
                left -= 1
                res.append(left)
        #print(res)
        return [i - left for i in res]