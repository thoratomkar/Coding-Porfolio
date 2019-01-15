def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def bst(current,res):
            if current is None:
                return
            
            bst(current.left,res)
            res.append(current.val)
            bst(current.right,res)
            return res
        
        
        res = []        
        bst(root,res)
       
        for i in range(1, len(res)):
            if res[i-1] >= res[i]:
                return False

        return True