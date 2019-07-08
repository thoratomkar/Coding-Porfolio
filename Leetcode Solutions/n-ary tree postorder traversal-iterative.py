def postorder(self, root: 'Node') -> List[int]:
        
        res =[]
        if root == None: 
            return res

        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)            

        return res[::-1]
        