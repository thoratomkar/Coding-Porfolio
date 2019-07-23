def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1 = sorted(arr1)
        ans = []
        temp = []
        for i in arr2:
            for j in range(len(arr1)):
                if arr1[j] == i:
                    ans.append(arr1[j])
                elif arr1[j] not in arr2:
                    temp.append(arr1[j])
       
        return ans+temp[:len(arr1)-len(ans)]