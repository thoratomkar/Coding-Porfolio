def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def _traverse(current,res):
            
            if current !=None:
                _traverse(current.left,res)
                res.append(current.val)
                _traverse(current.right,res)
            return res  
            
            
        if root == None:
            return True
        
        res =[]
        _traverse(root,res)
        if len(set(res))>1:
            return False
        return True