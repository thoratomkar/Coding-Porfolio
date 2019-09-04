def oddEvenList(self, head: ListNode) -> ListNode:
        
        if not head:
            return
        
        if head.next == None:
            return head
        
        temp = head.next
        index = 0
        h = head
        while head:
            x = head.next
            if head.next:
                
                head.next = head.next.next
                if head.next == None and index%2==0:
                    head.next = temp
                    break
                head = x
            else:
                head.next = temp
                break
            index+=1
            
                
        return h