class Solution:
    def height(self, current):
        
        if current:
            return 1 + max(self.height(current.left), self.height(current.right))
        
        return 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        if root is None: 
            return 0
        
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)
        
        return max(lheight + rheight, max(ldiameter, rdiameter))