def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
               
        def _search(current, value):
            if current.val == value:                
                return current
            elif value> current.val and current.right != None:
                return _search(current.right, value)
            elif value< current.val and current.left != None:
                return _search(current.left, value)
            else:
                return []
            
            
        
        return _search(root,val)