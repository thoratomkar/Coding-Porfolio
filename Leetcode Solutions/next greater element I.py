def nextGreaterElement(self, nums1, nums2):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        l = [-1]*len(nums1)
        index = 0
        for i in nums1:            
            temp = []            
            x = nums2.index(i)
            temp = nums2[x:]
            for j in (temp):
                if j>i:                
                    l[index] = j
                    break
            index +=1
        
        return l