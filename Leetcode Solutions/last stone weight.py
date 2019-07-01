def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort(reverse=True)
    
        while len(stones)>1:
            if stones[0]!=stones[1]:
                stones.append(abs(stones[0]-stones[1]))
                stones.remove(stones[0])
                stones.remove(stones[0])
                stones.sort(reverse=True)
            else:
                stones.remove(stones[0])
                stones.remove(stones[0])        

        if len(stones)>0:
            return stones[0]
        else:
            return 0