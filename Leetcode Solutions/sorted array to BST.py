def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(l, r):
            if l > r:
                return None
            i = (l + r) // 2
            root = TreeNode(nums[i])
            root.left = helper(l, i-1)
            root.right = helper(i+1, r)
            return root
        
        return helper(0, len(nums) - 1)