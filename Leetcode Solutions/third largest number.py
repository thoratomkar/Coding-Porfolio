def thirdMax(self, nums: List[int]) -> int:
        
        ans = [float('-inf'), float('-inf'), float('-inf')]
        
        for i in nums:
            
            if i not in ans:
            
                if i > ans[0]:
                    ans = [i, ans[0], ans[1]]

                elif i > ans[1]:
                    ans = [ans[0], i, ans[1]]

                elif i > ans[2]:
                    ans = [ans[0], ans[1], i]
        
        
        if float('-inf') in ans:
            
            return max(nums)
        
        return ans[2]
        