def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        l = []
        for i in range(19):
            for j in range(19):
                res = x**i + y**j
                if res<=bound and res not in l:
                    l.append(res)
        
        return l