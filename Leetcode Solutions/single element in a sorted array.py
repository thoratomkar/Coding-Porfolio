def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if mid %2 == 0:
                ## unique at right
                if nums[mid] == nums[mid+1]:
                    l = mid + 2
                else:
                    r = mid
            else:
                ## unique part at right
                if nums[mid] == nums[mid-1]:
                    l = mid + 1
                else:
                    r = mid-1

        return nums[l]