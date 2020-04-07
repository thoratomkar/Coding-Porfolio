def maxSubArray(self, nums: List[int]) -> int:
        '''
        currsum = nums[0]
        maxsum = nums[0]
        
        for i in range (1,len(nums)):
            
            currsum = max(nums[i], currsum + nums[i])
            maxsum = max(maxsum, currsum)
        
        
        return maxsum
        '''
       
        maxsum = currsum = nums[0]
        start= end = beg = 0
        
        for i in range(1,len(nums)):
            
            currsum += nums[i]
            
            if currsum < nums[i]:
                
                currsum = nums[i]
                beg = i + 1
            
            if maxsum < currsum:
                
                maxsum = currsum
                start = beg
                end = i
        print(nums[start:end+1])
        return maxsum
                