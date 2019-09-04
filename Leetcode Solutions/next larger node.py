def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        ans = []
        stack = []
        index = 0
        
        while head:
            ans.append(0)
            
            while stack and stack[-1][1] < head.val:
                last_val = stack.pop()
                ans[last_val[0]] = head.val
                
            stack.append((index,head.val))
            index+=1
            head = head.next
        
        return ans