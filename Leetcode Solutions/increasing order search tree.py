def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(current, res):
            if current != None:
                inorder(current.left,res)
                res.append(current.val)
                inorder(current.right,res)
                
        res = []
        inorder(root,res)
        
        ans = current = TreeNode(None) 
        for value in res:
            current.right = TreeNode(value)
            current = current.right 
        return ans.right