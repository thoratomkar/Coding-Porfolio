def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: 
            return []
        q = [[root]]
        for level in q:
            record = []
            for node in level:
                if node.left: 
                    record.append(node.left)
                if node.right: 
                    record.append(node.right)
            if record: 
                q.append(record)
        
        l =[]
        for level in q:
            temp = []
            for x in level:
                temp.append(x.val)
            l.append(temp)
        return l
                