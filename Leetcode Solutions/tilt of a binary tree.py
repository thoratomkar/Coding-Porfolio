def traverse(self, root, tilt): 
        if (not root):  
            return 0

        left = self.traverse(root.left, tilt)  
        right = self.traverse(root.right, tilt)  

        tilt[0] += abs(left - right)  

        return left + right + root.val 
  
    
    def findTilt(self, root: TreeNode) -> int:
        tilt = [0] 
        self.traverse(root, tilt)  
        return tilt[0] 