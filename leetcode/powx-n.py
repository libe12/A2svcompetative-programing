class Solution: 
  
    def myPow(self, x, n):
            if n == 0:          return 1                     # Handle with special case
            elif n < 0:         return 1.0 / self.myPow(x, -n) # Handle with negative n
            elif n == 1:        return x                     # Termination condition
            else:
                # Recursive condition
                if n % 2 == 0:  return self.myPow(x*x, n//2)
                else:           return self.myPow(x*x, n//2)*x
