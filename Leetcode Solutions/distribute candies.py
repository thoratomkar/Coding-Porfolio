def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        total = len(candies)
        dic = {}
        candies_set = set(candies)
        
            
        
        diff_candies = len(candies_set)
        
        if diff_candies > total/2:
            return total/2
        
        return diff_candies 