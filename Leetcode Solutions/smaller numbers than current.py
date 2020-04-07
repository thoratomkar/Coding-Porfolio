def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sortedlist = sorted(nums)
        ans = []
        for i in nums:
            ans.append(sortedlist.index(i))
        
        return ans