def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        #return [i if nums.count(i) == 2: for i in nums]
        for n in nums:
            ind = abs(n) - 1
            if nums[ind] < 0:
                l.append(abs(n))
            nums[ind] = - nums[ind]
        return l