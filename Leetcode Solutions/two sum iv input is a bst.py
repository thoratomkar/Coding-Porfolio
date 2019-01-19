def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        def traversal(current,res):
            if current !=None:
                traversal(current.left,res)
                res.append(current.val)
                traversal(current.right,res)
        
        res = []
        traversal(root,res)
        
        for i in range(len(res)):
            if k - res[i] in res[i+1:]:
                return True
        return False