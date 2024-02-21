class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        c = Counter(answers)
        ans = 0
        for n in c:
            if n == 0:
                ans += c[n]
            elif (c[n]-1)<=n:
                ans += n+1
            else:
                while n!=0 and n < c[n]:
                    ans += n+1
                    c[n] -= (n+1)
                if c[n]!=0 and c[n]<=n:
                    ans += n+1
        return ans
