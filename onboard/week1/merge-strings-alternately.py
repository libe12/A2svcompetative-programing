class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        res = []
        p1 = p2 = 0
        while p1<w1 or p2<w2:
            if p1<w1:
                res += word1[p1]
                p1+=1
            if p2<w2:
                res += word2[p2]
                p2+=1
        return ''.join(res)