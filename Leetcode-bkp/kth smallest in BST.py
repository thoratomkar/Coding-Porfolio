def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        def _traversal(current,res):
            
            if current == None:
                return
            _traversal(current.left,res)
            res.append(current.val)
            _traversal(current.right,res)
            
            return res
        
        res = []
        _traversal(root,res)
        
        return res[k-1]