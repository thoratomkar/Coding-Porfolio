def maxDepth(self, root: 'Node') -> int:
        
        if not root:
            return 0
        
        stack = [root]
        depth = 0
        
        while stack:
            l = []
            while stack:        
                curr = stack.pop()                
                l += curr.children
            stack = l
            depth +=1
        
        return depth