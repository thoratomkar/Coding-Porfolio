def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        
        answer = []
        total=0
        for i in A:
            if i%2==0:
                total+=i
        for i in queries:
            #print(i)
            
            prev = A[i[1]] 
            A[i[1]] = i[0]+A[i[1]]
            #print(A[i[1]])
            #print(A)
            if prev %2 == 0:
                total -= prev
            if A[i[1]]%2 == 0:
                total += A[i[1]]
            answer.append(total)