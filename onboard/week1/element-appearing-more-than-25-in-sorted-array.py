class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        res = (max(count.values()))
    
        for num in arr:
            if count[num] == res:
                return num