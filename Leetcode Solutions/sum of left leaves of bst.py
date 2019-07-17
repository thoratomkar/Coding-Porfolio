 def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        stack = [root]
        answer = 0
        
        while stack :
           
            temp = stack.pop()
            
            if temp.left:
                
                if not temp.left.left and not temp.left.right:
                    answer += temp.left.val
                stack.append(temp.left)
            
            if temp.right:                
                stack.append(temp.right)
        
        return answer