def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """    
       
        self.preorder = []
        
        def traverse(node):           
            
            if not node:
                return            
            
            self.preorder.append(node.val)
            
            if node.children:
                for child in node.children:
                    traverse(child)       
       
        traverse(root)
    
        return self.preorder