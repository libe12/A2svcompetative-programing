class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = defaultdict(int)
        for j in range(100000):
            d[str(j)]=1
        for i in range(26):
            res = chr(ord('a')+i)
            arr = chr(ord('A')+i)

            d[res] = 1
            d[arr] =1
        result = []
        for i in s:
            if i in d :
                result.append(i)
        output = ''.join(result)
      
        if output.lower() == ''.join(reversed(output.lower())):

            return True

        return False
                

        


       