class Solution:
    def numberOfMatches(self, n: int) -> int:
        tot =0
        res = n
        for _ in range(n):
            if res == 1:
                break
                
            elif (res%2)==0:
                res = res//2
                tot += res
                
            elif res % 2 ==1:
                res = (res+1)//2
                tot += (res-1)
               
        return tot


        