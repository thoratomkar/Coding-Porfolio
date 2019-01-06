def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        return len(nums)!=len(set(nums))
        """
        
        l = sorted(nums)
        for i in range(len(l)-1):
            if l[i] == l[i+1]:
                return True
        return False