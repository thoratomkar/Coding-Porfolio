def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        previous = None
        if head == None:
            return
        
        elif head.next == None:
            return head
        
        else:
            
            while current:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            self.head = previous
            return self.head