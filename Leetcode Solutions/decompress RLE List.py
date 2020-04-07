def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for i in range (0,len(nums),2):
            for j in [nums[i+1]]*nums[i]:
                
                ans.append(j)
            
        return ans