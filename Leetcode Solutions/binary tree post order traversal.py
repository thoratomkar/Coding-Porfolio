def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def _traversal(current,res):
            if current != None:
                _traversal(current.left,res)
                _traversal(current.right,res)
                res.append(current.val)
            return res
        
        res = []
        
        return _traversal(root,res)