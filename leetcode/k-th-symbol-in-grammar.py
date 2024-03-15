class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if k == 1:
            return 0
        if k % 2 == 1:
            return self.kthGrammar(n-1,ceil(k/2))
        val = self.kthGrammar(n-1,ceil(k/2))

        if val:
            return 0
        else:
            return 1
        

    
        