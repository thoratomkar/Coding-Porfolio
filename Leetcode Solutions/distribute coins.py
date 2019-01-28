def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        def dfs(node):
            if node !=None:
                L, R = dfs(node.left), dfs(node.right)                
                self.count += abs(L) + abs(R)                
                return node.val + L + R - 1
            else:
                return 0                     
        
        dfs(root)
        return self.count