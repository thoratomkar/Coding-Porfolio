def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def getLeaves(root):
            visited=[root]
            res=[]
            while len(visited)>0:
                node=visited.pop()
                if node.left:
                    visited.append(node.left)
                if node.right:
                    visited.append(node.right)
                if not node.left and not node.right:
                    res.insert(0,node.val)
            print(res)
            return res
        
        return getLeaves(root1) == getLeaves(root2)