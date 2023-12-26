class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        di = defaultdict(list)
        for i,num in enumerate(arr1):
            di[num].append(num)
        
        d2  = defaultdict(list)
        for i, num in enumerate(arr2):
            d2[num] = i
        
        arr = []
        add = []
        for i,num in enumerate(arr2):
            if num in di:
                arr+=di[num]
            
        for num in di:
            if num not in d2:
                add+=di[num]
        return arr+sorted(add)

        