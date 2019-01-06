def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums): 
            return 0 #If there are no houses to rob, return 0; BASE Case

        dp = [0] * (len(nums)) # Dp is of size num of houses
        dp[0] = nums[0] # Base case, if there is only 1 house then the profit is the house' value

        if len(nums) > 1: # If there are more than 1 houses
            dp[1] = max(nums[:2]) # Compute the profit of robbing just two houses, its max of those houses
            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1]) # Max of sum of house 1, 3 and house 2

        return dp[-1] # Return the profit after robbing all houses