def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        price = 0
        temp = sorted(prices, reverse=True)
        if prices ==[] or temp == prices:
            return 0
        
        while prices !=[]:
            
            max_price = max(prices)
            index = prices.index(max_price)
            if index!=0:
                
                price = max(price, max_price - min(prices[:index]))
                
            prices.pop(index)

            
        return price
        """
        if (len(prices) == 0):
            return 0;
        
        mini= prices[0];
        profit= 0;
        for i in range(1,len(prices)):
            profit = max(profit, prices[i] - mini);
            mini = min(mini, prices[i]);
        
        return profit;