def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()        
        while (head): 
             
            if (head in s):                 
                return True

            s.add(head) 
            head = head.next

        return False