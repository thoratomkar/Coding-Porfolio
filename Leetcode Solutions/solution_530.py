# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
       
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #current = root
        l=[]
        def _getMinimumDifference(current):
            
            if current != None:
                _getMinimumDifference(current.left)
                l.append(current.val)
                _getMinimumDifference(current.right)
                
        
        if root != None:
            _getMinimumDifference(root)
            def find_min_diff(l):
                diff = 10**20
                for i in range(0,len(l)-1):
                    if l[i+1] - l[i] < diff:
                        diff = l[i+1] - l[i]
                return diff
            return(find_min_diff(l))
        else:
            return