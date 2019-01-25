def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if(t == None):
            return ""
        if(t.left == None and t.right == None):
            return str(t.val)
        s = str(t.val) + "(" + self.tree2str(t.left) + ")";
        if t.right != None:
            
            s = s + "(" + self.tree2str(t.right) + ")";
        return s;