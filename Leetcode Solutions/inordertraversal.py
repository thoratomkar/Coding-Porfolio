def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        
        
        def _inorderTraversal(current, l):
            if current != None:
                _inorderTraversal(current.left, l)
                l.append(current.val)                 
                _inorderTraversal(current.right,l)
                
                
            
                
        l = []
        _inorderTraversal(root, l)
        return l
        """
        result = []
        
        if root == None:
            return result
        else:

            p = root
            stack = []

            while stack or p:
                while p:
                    
                    stack.append(p)
                    p = p.left
                p = stack.pop()
                result.append(p.val)
                p = p.right
                
        return result