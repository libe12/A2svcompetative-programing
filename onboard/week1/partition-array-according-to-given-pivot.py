class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res1 = []
        res2 = []
        res3 = []
        for num in nums:
            if num > pivot:
                res2.append(num)
            elif num < pivot:
                res1.append(num)
            else:
                res3.append(num)
        res = res1 + res3 + res2
        return res

        