def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traversal(current,res):
            if current != None:
                traversal(current.left,res)
                if current.val not in res:
                    res.append(current.val)
                traversal(current.right,res)
                
        res = []
        traversal(root,res)
        res.sort()
        if len(res) == 1:
            return -1
        return res[1]