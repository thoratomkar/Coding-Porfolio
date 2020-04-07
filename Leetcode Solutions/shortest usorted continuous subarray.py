def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        if len(nums) < 2: 
            return 0
        
        l = 0
        r = len(nums) - 1
        
        while l < len(nums) -1 and nums[l] <= nums[l+1]:            
            l+=1
        
        while r > 0 and nums[r] >= nums[r-1]:            
            r-=1
            
        if l>r:
            return 0
        
        temp = nums[l:r+1]
        
        tempmin = min(temp)
        tempmax = max(temp)
        
        while l>0 and nums[l-1]>tempmin:
            
            l -=1
            
        while r<len(nums)-1 and nums[r+1]<tempmax:
            
            r +=1
            
        return r-l+1
    
        
         