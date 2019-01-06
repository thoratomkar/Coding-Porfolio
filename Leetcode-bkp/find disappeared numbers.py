def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        for i in range(len(nums)):
            val = abs(nums[i]) - 1;
            if(nums[val] > 0):
                nums[val] = -nums[val];
           
        
        for i in range(len(nums)):
            if(nums[i] > 0):
                l.append(i+1);
          
        return l;