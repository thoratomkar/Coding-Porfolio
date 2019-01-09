def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        
        return zip(*A)
        """
        R = len(A)
        C = len(A[0])
        transpose = []
        for c in range(C):
            newRow = []
            for r in range(R):
                newRow.append(A[r][c])
            transpose.append(newRow)
        return transpose