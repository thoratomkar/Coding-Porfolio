def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def traversal(current,res,l,r):
            if current != None:
                traversal(current.left,res,l,r)
                if current.val >= l and current.val<=r:
                    res.append(current.val)
                traversal(current.right,res,l,r)
        res = []
        traversal(root,res,L,R)
        return sum(res)