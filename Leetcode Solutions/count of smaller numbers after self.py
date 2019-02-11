def countSmaller(self, nums: 'List[int]') -> 'List[int]':
        if nums == []:
            return []
        out = [0]*len(nums)
        temp = []
        temp.append(nums[-1])
        i = len(nums)-2
        while i>=0:
            count = 0
            temp.append(nums[i])
            for j in temp:
                if j< nums[i]:
                    count+=1
            out[i] = count
            i -=1
        
        return out
                