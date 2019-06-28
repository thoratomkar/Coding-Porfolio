def removeOuterParentheses(self, S: str) -> str:
        stack = []
        str = ""        
        for n in S:
            if n == ")":
                stack.pop()
            if stack:
                str += n
            if n == "(":
                stack.append(n)
        
        return str