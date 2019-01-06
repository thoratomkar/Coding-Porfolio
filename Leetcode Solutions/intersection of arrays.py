def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l = []
        i=-1
        j=-1
        if len(nums1)-1 <= len(nums2)-1:
            i = len(nums1)-1
        else:
            j = len(nums2)-1
        
        if i < j:
            while j>=0:
                if nums2[j] in nums1:
                    l.append(nums2[j])                    
                    nums1.remove(nums2[j])
                    nums2.remove(nums2[j])
                    j -=1
                else:
                    j-=1
        else:
            while i>=0:
                if nums1[i] in nums2:
                    l.append(nums1[i])
                    nums2.remove(nums1[i])
                    nums1.remove(nums1[i])                    
                    i -=1
                else:
                    i-=1
        return l