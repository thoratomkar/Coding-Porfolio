class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = [float('inf')]
        self.min = float('inf')
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        m = self.min
        if x < m:
            self.min = x
            self.minStack.append(x)
        else:
            self.minStack.append(m)
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        minStack = self.minStack
        minStack.pop()
        self.min = minStack[-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()