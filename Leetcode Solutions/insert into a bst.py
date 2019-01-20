def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def _insert(current,val):
            if current != None:
                if val > current.val:
                    if current.right == None:
                        current.right = TreeNode(val)
                    else:
                        _insert(current.right,val)
                else:
                    if current.left == None:
                        current.left = TreeNode(val)
                    else:
                        _insert(current.left,val)
        
        if root != None:
            _insert(root,val)
            return root
        else:
            root = TreeNode(val)
            return root