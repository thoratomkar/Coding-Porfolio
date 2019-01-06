def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        
        maxheap = []
        
        for i in range(len(nums)):
            maxheap.append((-nums[i])) # Negative for maxheap
            
        heapq.heapify(maxheap)
        
        largest = []
        for i in range(k):
            largest.append(-heapq.heappop(maxheap))
        return largest[-1]

def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums == []:
            return
        else:
            nums.sort()
            return nums[len(nums)-k]