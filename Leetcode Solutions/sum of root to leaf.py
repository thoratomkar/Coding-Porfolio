def sumRootToLeaf(self, root: TreeNode) -> int:
        
        stack, res = [(root, str(root.val))], 0
        
        while stack:
            
            node, parent_val = stack.pop()
            if not node.left and not node.right:
                res += int(parent_val, 2)
                continue
            
            if node.left: 
                stack.append((node.left, parent_val + str(node.left.val)))
            if node.right: 
                stack.append((node.right, parent_val + str(node.right.val)))
        
        return res