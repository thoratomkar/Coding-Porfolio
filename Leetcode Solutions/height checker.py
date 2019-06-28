def heightChecker(self, heights: List[int]) -> int:
        
        x = sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!=x[i]:
                count +=1
                
        return count