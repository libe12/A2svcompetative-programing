class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 0, x
        
        if x==0 or x==1:
            return x
        while left  <= right:

            mid = (left + right)//2

            if mid * mid > x:
                right = mid-1
                
            elif mid*mid==x:
                return mid
            else:
                left = mid+1
               
        return right
        