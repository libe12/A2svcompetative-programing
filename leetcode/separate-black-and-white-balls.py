class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        tar = 0
        for one in s:
            if one == '1':
                tar += 1
            else:
                ans += tar
        return ans