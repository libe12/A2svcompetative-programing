class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        val = len(s1)
        ans = 0
        if len(s1)>len(s2):
            return False
        for r in range(len(s1)):
            if s2[r] in s1:
                ans +=1
                if ans ==val and sorted(s1)==sorted(s2[:val]):
                    return True
        for r in range(val,len(s2)):
            if s2[r] in s1:
                ans+=1
            if s2[r-val] in s1:
                ans-=1
           
            if ans==val and sorted(s1)==sorted(s2[r-val+1:r+1]):
                print(r)
                return True
        return False
        