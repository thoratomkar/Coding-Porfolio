class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index=0
        
        while index<len(nums):
            if nums[index]==target:
                return index
            index+=1
        
        for i in range(0,len(nums)):
            if target<nums[i]:
                return i
            
        return i+1