class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        if n == 1:
            return '0'
        if 2**n/2 == k/1:
            return '1'

        if k <= (2**n-1)//2:

            return self.findKthBit(n-1,k)
        
        val = self.findKthBit(n-1,2**n-k)
        print(n,val)
        if val == '0':
            return '1'
        else:
            return '0'

        