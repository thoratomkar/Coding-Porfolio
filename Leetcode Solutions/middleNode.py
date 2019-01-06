def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        l = []
        count =0
        while head:
            l.append(head.val)
            count +=1
            head = head.next
        
        x = count//2
        return l[x:]
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
            