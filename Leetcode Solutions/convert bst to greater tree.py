def convertBST(self, root: TreeNode) -> TreeNode:
        
        def dfs(node,val):#return cumu sum of this node.
            if not node:
                return val
            val=dfs(node.right,val)
            node.val+=val
            return dfs(node.left,node.val)
        dfs(root,0)
        return root