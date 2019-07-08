def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        
        def leaves (root):
            if root == None:
                return []

            ans = []
            stack = []
            leaf = []

            while stack or root:
                if root:
                    stack.append(root)
                    if root.left == None and root.right == None:
                        leaf.append(root.val)

                    root = root.left
                else:
                    curr = stack.pop()
                    ans.append(curr.val)
                    root = curr.right
            return leaf
        
        return leaves(root1) == leaves(root2)