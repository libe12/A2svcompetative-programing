class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        r = len(piles)-2
        res=0
        while r >=len(piles)//3:
            
            res += piles[r]
            
            r-=2
        return res

        