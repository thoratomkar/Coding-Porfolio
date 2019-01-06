# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """             
        if l1 == None:
            return l2
        elif(l2 == None):
            return l1
        elif(l1.val < l2.val):
            result = l1
            result.next = self.mergeTwoLists(l1.next, l2)
            
        else:
            result = l2
            result.next = self.mergeTwoLists(l1, l2.next)
            
        return result