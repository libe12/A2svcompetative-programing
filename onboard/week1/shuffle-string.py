class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        update_char=[0]*len(s)
        for i in range(len(s)):
            update_char[indices[i]]=s[i]
        result = ''.join(update_char)
        return result