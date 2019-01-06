# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        else:
            previous = head
            current = head.next
            while current != None:
                if current.val == previous.val:
                    temp=current.next
                    previous.next = temp
                    current = None
                    current = temp

                else:    
                    previous = current
                    current = current.next
            return head
            