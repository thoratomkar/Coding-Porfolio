class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        m=9999999999
        if x<m:
            self.items.append(x)
            m=x
    def pop(self):
        """
        :rtype: void
        """
        self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def getMin(self):
        """
        :rtype: int
        """
        index=0
        minimum=9999999999
        while index <len(self.items):
            if self.items[index]<minimum:
                minimum=self.items[index]
                index+=1
            else:
                index+=1
        return minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()