class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        bound = max(arr)
        idx = arr.index(bound)
        if len(arr) == 1:
            return False
        for i in range(len(arr)-1):
            if idx == 0 or idx == len(arr)-1:
                return False
            elif i < idx:
                if arr[i+1] <= arr[i]:
                    return False
                    break
                    
            if i >= idx:
                if arr[i] <= arr[i+1]:
                    return False
                    break
        return True


        