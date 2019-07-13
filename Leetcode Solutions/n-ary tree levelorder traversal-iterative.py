def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        answer = []
        if root == None:
            return answer
        stack = [root]
        
        while stack:
            level = []
            t = []
            for i in stack:
                level+=(i.children)
                t.append(i.val)
            answer.append(t)
            stack = level
        
        return answer