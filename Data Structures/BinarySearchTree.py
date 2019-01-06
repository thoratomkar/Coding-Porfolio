# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:41:06 2018

@author: omkar
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent=None
class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)
            
    def _insert(self,value,current_node):
        if value < current_node.value:
            if current_node.left == None:
                   current_node.left = Node(value)
                   current_node.left.parent=current_node
            else:
                  self._insert(value,current_node.left)
        
        elif value > current_node.value:
              
            if current_node.right == None:
                current_node.right = Node(value)
                current_node.right.parent=current_node
            else:
                self._insert(value,current_node.right)
                
        else:
            print(f'{value} already present in tree')
            
    def display(self):
        if self.root != None:
            self._display(self.root)
            
    def _display(self, current_node):
        
        if current_node!=None:
            self._display(current_node.left)
            print(current_node.value)
            self._display(current_node.right)
            
    def height(self):
        if self.root != None:
           return self._height(self.root,0)
        else:
            return 0
        
    def _height(self,current_node,height):
        if current_node == None:
            return height
        left_height=self._height(current_node.left,height+1)
        right_height=self._height(current_node.right,height+1)
        return max(left_height,right_height)
    
    def search(self,value):
        if self.root != None:
            return self._search(self.root,value)
        else:
            return False
    
    def _search(self,current_node,value):
        if current_node.value == value:
            return True
        elif value<current_node.value and current_node.left != None:
            return self._search(current_node.left,value)
        elif value>current_node.value and current_node.right != None:
            return self._search(current_node.right,value)
        else:
            return False
        
    def traversal(self,order):
        if self.root != None:
            self._traversal(self.root,order)
        return "Tree Empty"
    
    def _traversal(self,current_node,order):
        if order == 'Inorder':
            #print('Inorder Traversal\n')
            if current_node!=None:
                self._traversal(current_node.left,order)
                print(current_node.value)
                self._traversal(current_node.right,order)
                
        elif order == 'Preorder':
            #print('Preorder Traversal\n')
            if current_node!=None:
                print(current_node.value)
                self._traversal(current_node.left,order)
                self._traversal(current_node.right,order)
                
        else:
            #print('Postorder Traversal\n')
            if current_node!=None:
                self._traversal(current_node.left,order)
                self._traversal(current_node.right,order)
                print(current_node.value)
                
    def klargest_element(self, k):
        if self.root == None:
            return 'Tree is Empty'
        else:
            s = []
            count = 0
            current_node = self.root
            while current_node != None or s != []:
                if current_node != None:
                    s.append(current_node)
                    current_node = current_node.right
                else:
                    inorder_node = s.pop()
                    count += 1
                    if count == k:
                        return inorder_node.value
                    current_node = inorder_node.left
                    
            
            
                
tree = BinarySearchTree()

tree.insert(30) 
tree.insert(20) 
tree.insert(40) 
tree.insert(70) 
tree.insert(80) 
tree.insert(60)
tree.insert(50)
#tree.display()
print(tree.height())
print(tree.search(10))
print(tree.search(80))
print('Inorder Traversal')
tree.traversal('Inorder')
print('Preorder Traversal')
tree.traversal('Preorder')
print('Postorder Traversal')
tree.traversal('Postorder')
print('k largest element is:')
k=tree.klargest_element(4)
print(k)