def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        count = 0
       
        for i in range(0,len(nums)):
            if nums[i]==0:
                count +=1
        
        while count>0:
            nums.remove(0)
            nums.append(0)
            count -=1
        '''
        slow = 0
        fast = 0
        
        while fast < len(nums):
            
            if nums[slow] == 0 and nums[fast] != 0:
                
                #nums[slow], nums[fast] = nums[fast], nums[slow]                
            
            if nums[slow] != 0:
                
                slow += 1
                
            fast += 1