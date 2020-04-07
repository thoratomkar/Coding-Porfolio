def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        n = len(nums) 
        k = k % n
        
        nums[:] = nums[n-k:] + nums[:n-k]
        '''
        def reverse(nums, start, end):
            
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1
        
        
        k = k % len(nums)
        
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)