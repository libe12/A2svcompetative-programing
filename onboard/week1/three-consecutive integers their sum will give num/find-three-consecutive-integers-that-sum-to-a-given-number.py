class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        arr = num//3
        print(arr)
        if (arr-1) + (arr) + (arr+1) == num:
            return [arr-1, arr, arr+1]
        return []