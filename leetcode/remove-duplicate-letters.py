class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s)
        my_set = set()
        ans = []
        for i in range(len(s)):
            
            while ans and freq[ans[-1]] > 0 and ord(ans[-1]) > ord(s[i]) and s[i] not in my_set:
                res = ans.pop()
                my_set.discard(res)
                
            if s[i] not in my_set:
                my_set.add(s[i])
                ans.append(s[i])

            freq[s[i]] -= 1
        
        return ''.join(ans)


        