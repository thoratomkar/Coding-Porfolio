def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
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
        '''
        i = 0 
        buy = sell = profit = 0
        N = len(prices) - 1;
        while (i < N):
            while (i < N and prices[i + 1] <= prices[i]):
                i+=1;
            buy = prices[i];

            while (i < N and prices[i + 1] > prices[i]):
                i+=1;
            sell = prices[i];

            profit += sell - buy;
        
        return profit;
        