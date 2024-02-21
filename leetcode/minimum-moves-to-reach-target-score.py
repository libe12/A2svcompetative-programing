class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        n = maxDoubles
        tar = target
        ans = -1
        while tar > 0:
            if tar %2 == 0:
                if n>0:
                    ans += 1
                    tar = tar//2
                    n-=1
                else:
                    ans += tar
                    break
            else:
                tar -= 1
                ans += 1
        return  ans
        