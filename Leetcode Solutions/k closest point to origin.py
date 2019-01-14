def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        l = []
        for i in points:
            dist = (i[0]**2 + i[1]**2)**0.5
            l.append((dist,i))
        res = sorted(l, key=lambda x: x[0])
        
        final = [x[1] for x in res]
        
        return (final[:K])