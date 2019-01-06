def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        l = []
        stack = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < stack:
                stack = prices[i]
            else:
                l.append(prices[i] - stack)
                stack = prices[i]
        return sum(l)