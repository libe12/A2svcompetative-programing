class Solution:
    def minimizedStringLength(self, s: str) -> int:
        set_lim = set(s)
        len_set = len(set_lim)
        return len_set