def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        
        l = [0]*len(T)
        for i in range(len(T)-1):
            count = 1
            for j in range(i+1,len(T)):
                
                if T[j]>T[i]:
                    l[i] = count
                    break
                else:
                    count+=1
        return l
        """
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans