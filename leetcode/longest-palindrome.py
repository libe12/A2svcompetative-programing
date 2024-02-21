class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)


        ans = 0
        r = 0
        for ch in count:
            if count[ch] % 2 == 0:
                ans += count[ch]
            else:
                r = 1
                ans += (count[ch]-1)
        
        return ans + r



        