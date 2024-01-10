class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        tot = sum(cardPoints[:])
        wind = sum(cardPoints[:n-k])
        ans = tot-wind
        for i in range(n-k,n):
            wind = wind - cardPoints[i+k-n] + cardPoints[i]
            ans = max(ans, tot-wind)
        return ans