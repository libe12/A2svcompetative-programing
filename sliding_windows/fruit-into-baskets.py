class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(fruits)):
            d[fruits[r]] += 1
            while len(d) > 2:
                
                d[fruits[l]] -= 1
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l += 1
            res  = max(res,r-l+1)
        return res
            


        