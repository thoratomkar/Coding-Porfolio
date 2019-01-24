def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        left = 1
        right = n
        while left <= right:
            mid = (left + right)//2
            if isBadVersion(mid) == True:
                if isBadVersion(mid-1) == True:
                    right = mid -1
                else:
                    return mid
            else:
                left = mid + 1