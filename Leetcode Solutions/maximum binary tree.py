def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])
        pivot = max(nums)
        print(pivot)
        idx = nums.index(pivot)
        ret = TreeNode(pivot)
        ret.left = self.constructMaximumBinaryTree(nums[:idx])
        ret.right = self.constructMaximumBinaryTree(nums[idx+1:])

        return ret