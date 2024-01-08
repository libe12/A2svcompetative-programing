class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        l =  0
        intial = 0
        vowel= 'aeiou'

        for r in range(len(s[:k])):
            if s[r] in vowel:
                intial += 1

        updated = intial
        for r in range(k,len(s)):
            if s[l] in vowel:
                intial -=1
            if s[r] in vowel:
                intial +=1

            if intial > updated:
                updated = intial
            l +=1
        return updated
