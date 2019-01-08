def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def _traversal(current,res):
            if current != None:
                res.append(current.val)
                _traversal(current.left,res)
                _traversal(current.right,res)
                
            return res
        
        res = []
        
        return _traversal(root,res)