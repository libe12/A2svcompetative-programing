class Solution:
    def maxConsecutiveAnswers(self, ans: str, k: int) -> int:
        l=0
        res=0
        
        d={"T":0, "F":0}
        for r in range(len(ans)):
            d[ans[r]]+=1
            while d["T"]>k and d["F"]>k:
                d[ans[l]]-=1
                l+=1
            res=max(res, r-l+1)

        
        return res
        


