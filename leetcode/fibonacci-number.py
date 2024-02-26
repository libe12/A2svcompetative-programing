class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        one = Solution.fib(self,n-2)
        two = Solution.fib(self,n-1)
        return one + two
        