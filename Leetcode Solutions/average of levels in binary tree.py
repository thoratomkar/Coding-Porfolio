def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        if root == None:
            return None
        answer = [root.val]
        stack = [root]
        
        while stack:
            level = []
            c = 0
            total = 0
            for i in stack:
                if i.left != None:
                    level.append(i.left)
                    total += i.left.val
                    c += 1
                    
                if i.right != None:
                    level.append(i.right)
                    total += i.right.val
                    c += 1
            stack = level
            if c>0:
                answer.append(total/c)
        
        return answer