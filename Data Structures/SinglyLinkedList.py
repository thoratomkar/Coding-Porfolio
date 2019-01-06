# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:07:34 2018

@author: swats
"""

#delete element greater than key
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None      

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current=current.next
    
    def insert(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        last_node=self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node
        
    def prepend(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        new_node.next = current
        self.head = new_node
        
    def insert_before(self,data,key):
        new_node=Node(data)
        current = self.head
        previous = None
        if current.data == key:
            self.prepend(data)
            return
        while current:
            if current.data == key:
                #previous = current
                previous.next = new_node  
                new_node.next = current
            previous = current
            current = current.next
            
    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def delete(self,key):
        current = self.head
        previous = None
        if current.data == key and current.next != None:
            self.head = current.next
            current = None
            return
        else:
            while current:
                if current.data == key:
                    temp = current.next
                    previous.next = current.next
                    current.next = None
                    current = None
                    current = temp
                else:
                    previous = current
                    current = current.next
                
    def delete_elements_greater_than_key(self,key):
        current = self.head
        previous = None
        while current.data > key:
            temp = self.head
            current = temp.next
            self.head = None
            self.head = current
            if current is None:
                print('All Elements were Deleted')
                return
            #current = current.next
            
        #previous = self.head
        while current:
            if current.data > key:
                previous.next = current.next
                #current.next = None
                current = None
                current = previous
                current = current.next
            else:
                             
                previous = current
                current = current.next

    def deleteDuplicates(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = self.head
        current = self.head.next
        while current != None:
            if current.data == previous.data:
                temp=current.next
                previous.next = temp
                current = None
                current = temp
            
            else:    
                previous = current
                current = current.next
            
    def reverse(self):
        current = self.head
        previous = None
        
        if current.next is None:
            return head
        else:
            while current:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            self.head = previous
            return
                

        
         
llist=LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(6)
llist.insert(3)
llist.insert(4)
llist.insert(5)
llist.insert(6)
llist.display() 
llist.delete(6)
#llist.insert(-2)
#llist.display()  
#llist.prepend(3)     
#llist.display()  
#llist.insert_before(4,3)
#llist.insert_after_node(llist.head.next,0)
#llist.delete_elements_greater_than_key(0)
llist.display()  
#print('List after removing Duplicates')    
#llist.deleteDuplicates()  
#llist.reverse()
#llist.display() 