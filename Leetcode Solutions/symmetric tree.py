class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(left, right): 
            if left and right:
                if left.val == right.val:
                    check1 = check(left.left, right.right)
                    check2 = check(left.right, right.left)
                    return check1 and check2
            return left is right
        
        if root:
            return check(root.left, root.right)
        return True