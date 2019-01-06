def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)/2
        d = {}
        for i in nums:
            if i in d.keys():
                d[i] +=1
            else:
                d[i] = 1
        
        for i in d.keys():
            if d[i]>l:
                return i