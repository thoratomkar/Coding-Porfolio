def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        answer = []
        stack = [root]
        answer.append([root.val])
        while stack:
            level = []
            temp = []
            for i in stack:
                if i.left != None:
                    level.append(i.left)
                    temp.append(i.left.val)
                if i.right != None:
                    level.append(i.right)
                    temp.append(i.right.val)            
            stack = level
            #print(level[::])
            if temp:
                answer.append(temp)
        
        return answer[::-1]