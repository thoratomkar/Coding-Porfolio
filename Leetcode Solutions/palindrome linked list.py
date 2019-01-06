def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        l = []
        while current:
            l.append(str(current.val))
            current = current.next
        
        return l == l[::-1]