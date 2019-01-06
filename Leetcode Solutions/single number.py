def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i in d.keys():
                d[i] +=1
            else:
                d[i] = 1
        
        for i in range(len(nums)):
            c=nums[i]
            if d[c]==1:
                return c