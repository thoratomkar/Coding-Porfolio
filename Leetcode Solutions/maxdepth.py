def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def _maxDepth(node):
            
            if node is None:
                return 0

            else:

                lDepth = _maxDepth(node.left) 
                rDepth = _maxDepth(node.right) 

                # Use the larger one 
                if (lDepth > rDepth): 
                    return lDepth+1
                else: 
                    return rDepth+1
        return _maxDepth(root)