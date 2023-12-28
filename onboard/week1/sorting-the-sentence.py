class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(' ')
        
        ans = []
        for i in range(1,len(arr)+1):
            for j in range(len(arr)):
                if i == int(arr[j][-1]):
                    ans.append(arr[j][:-1])
        res = ' '.join(ans)
        return res
        