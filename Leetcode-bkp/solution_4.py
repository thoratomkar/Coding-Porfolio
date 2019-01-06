class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1=len(nums1)
        length2=len(nums2)
        result=[]
        i=0
        j=0
        k=0
        while(i<length1 and j<length2):
            if(nums1[i]<nums2[j]):
                result.append(nums1[i])
                i +=1
            else:
                result.append(nums2[j])
                j+=1
            k+=1
        while(i<length1):
            result.append(nums1[i])
            i+=1
            k+=1
        
        while(j<length2):
            result.append(nums2[j])
            j+=1
            k+=1
        
        lengthr=len(result)
        if lengthr %2!=0:
            return result[lengthr//2]
        else:
            temp=lengthr//2
            res=(result[lengthr//2-1]+result[lengthr//2])/2.0
            return res