def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root != None:
            root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        
        return root