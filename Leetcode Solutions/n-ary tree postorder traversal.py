def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.preorder = []
        
        def traverse(node):           
            
            if not node:
                return            
            
            
            
            if node.children:
                for child in node.children:
                    traverse(child) 
            self.preorder.append(node.val)
       
        traverse(root)
    
        return self.preorder