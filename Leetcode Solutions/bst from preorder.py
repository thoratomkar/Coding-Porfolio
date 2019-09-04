def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        
        for value in preorder[1:]:
            
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            
            else:
                while stack and value > stack[-1].val:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        
        return root