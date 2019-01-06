def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        d = {}
        for i in nums:
            if i in d.keys():
                return i
            else:
                d[i] = 1
        
        for i in nums:
            if nums.count(i)>1:
                return i
        
        l= sorted(nums)
        for i,v in enumerate(l):
            if(l[i]==l[i+1]):
                return v
        return -1
        """
        l = sorted(nums)
        for i in range(len(l)-1):
            if l[i] == l[i+1]:
                return l[i]