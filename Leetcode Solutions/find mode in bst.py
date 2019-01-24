def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traversal(current, res):
            if current !=None:
                traversal(current.left,res)
                if current.val in res:
                    res[current.val]+=1
                else:
                    res[current.val] = 1
                traversal(current.right,res)
            return res
        
        res = {}
        traversal(root,res)
        
        count = 2
        prev_count =0
        l = []
        for i in res.keys():
            if res[i] >= count:
                if res[i] >prev_count and l !=[]:
                    l.pop()
                l.append(i)
                prev_count = res[i]
                count = res[i]
        if l == []:
            return list(res.keys())
        return l