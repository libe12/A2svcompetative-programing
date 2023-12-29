class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for idx in range(len(arr)):
            n = len(arr)
            max_val = max(arr[:n-idx])
            max_idx = arr.index(max_val)+1
            arr[:max_idx] = reversed(arr[:max_idx])
            res.append(max_idx)
            arr[:n-idx] = reversed(arr[:n-idx])
            res.append(n-idx)
        return res
        

        