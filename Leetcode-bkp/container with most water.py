def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        maxarea = 0
        area = 0
        for i in range(0,len(height)):
            #x = height[i]
            for j in range (i+1, len(height)):
                if height[i] >= height[j]:
                    area = (height[j]*(j-i))
                                    
                else:
                    area = height[i]*(j-i)
                if area > maxarea:
                    maxarea = area
                    #area = 0
        return maxarea
        """
        left = 0
        right = len(height) - 1
        maxWater = 0
        width = len(height) - 1

        while width > 0:
            if height[left] > height[right]:
                maxWater = max(maxWater, height[right] * width)
                right -= 1
            else:
                maxWater = max(maxWater, height[left] * width)
                left += 1
            width -= 1

        return maxWater