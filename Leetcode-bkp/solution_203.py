# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        current = head
        previous = None
        if head == None:
            
            return
        
              
        while current.val == val:
            temp = head                  
            current = temp.next
            head = None
            head = current
            if current is None:
                return head      
        while current:
            if current.val == val:
                temp = current.next
                previous.next = current.next
                current.next = None
                current = None
                current = temp
            else:
                previous = current
                current = current.next
                
        return head