class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        r = n
        while r >= 1:
            if r == 1:
                return True
            r = r /4
            
        return False
        