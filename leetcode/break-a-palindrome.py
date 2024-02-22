class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        notpal = list(palindrome)
        n= len(notpal)
        if n==1:
            return ""
        for i in range(n):
            if notpal[i]!='a':
                notpal[i] = 'a'
                break
        
        if notpal!=notpal[::-1]:
            print(notpal)
            return ''.join(notpal)
        res = list(palindrome)
        for i in range(n-1,-1,-1):
            if res[i]=='a':
                res[i]='b'
                break
        return ''.join(res)
        
        