def maxDepth(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        stack = [root]
        depth = 0
        
        while stack:
            
            l = []
            for i in stack:
                if i.right != None:
                    l.append(i.right)
                if i.left != None:
                    l.append(i.left)
            
            stack = l
            depth +=1
        
        return depth