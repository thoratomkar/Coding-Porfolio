def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while(node.next!=None):
            node.val = node.next.val
            if(node.next.next!=None):
                node=node.next
            else:
                node.next=None
                break