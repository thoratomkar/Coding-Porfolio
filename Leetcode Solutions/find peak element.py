def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        
        
        
        count =0
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                count+=1
                return i
        if count == 0:
            return nums.index(max(nums))
        """
        i = 0
        j = len(nums)-1
        while (j-i)>1:
            k = int((i+j)/2)
            if nums[k]>nums[k-1] and nums[k]>nums[k+1]:
                return k
            elif nums[k]<nums[k-1]:
                j = k
            else:
                i = k
        if nums[j]>nums[i]:
            return j
        else:
            return i