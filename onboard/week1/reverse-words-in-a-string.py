class Solution:
    def reverseWords(self, s: str) -> str:

        res = s.split()
        arr = res[::-1]
        reversedWords = ' '.join(arr)
        return reversedWords
        
        