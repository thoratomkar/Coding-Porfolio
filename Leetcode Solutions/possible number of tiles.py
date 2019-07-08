from itertools import combinations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        l = []
        res = []
        for i in tiles:
            l.append(i)
        for i in range(len(l)+1):
            for subset in combinations(l, i):
                res.append(subset)
        return len(list(res))