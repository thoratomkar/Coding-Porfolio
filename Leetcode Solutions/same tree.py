def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def traversal(current,res):
            if current != None:
                res.append(current.val)
                if current.left == None:
                    res.append('NULL')
                traversal(current.left,res)
                if current.right == None:
                    res.append('NULL')
                traversal(current.right,res)
        res1 = []
        res2 = []
        
        traversal(p,res1)
        traversal(q,res2)
        
        return res1==res2

        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
        """