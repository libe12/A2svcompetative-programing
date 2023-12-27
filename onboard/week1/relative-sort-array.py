class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l = len(arr2)
        d = defaultdict(lambda:l)
        for i,num in enumerate(arr2):
            d[num] = i
        arr1.sort(key=lambda  x:(d[x],x))

        return arr1