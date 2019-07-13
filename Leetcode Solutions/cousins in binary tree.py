def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        stack = [(-1,root)]
        
        while stack:
            hs = {}
            level = []
            for i in stack:
                parent, node = i 
                hs[node.val] = parent
                if node.left != None:
                    level.append((node.val,node.left))
                    #hs[node.val] = parent
                    
                    
                if node.right != None:
                    level.append((node.val,node.right))
                    
            stack = level
            
            if x in hs and y in hs:
                if hs[x] != hs[y]:
				
                    return True
                else:
					
                    return False
        return False