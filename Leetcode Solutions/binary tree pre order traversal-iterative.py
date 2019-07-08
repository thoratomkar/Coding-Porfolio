def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        ans = []
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                ans.append(root.val)
                root = root.left
            else:
                tempnode = stack.pop()
                root = tempnode.right               
        
        return ans