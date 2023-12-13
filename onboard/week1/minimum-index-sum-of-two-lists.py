class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        min_sum = float('inf')
        for i, strs in enumerate(list1):
            if strs in list2:
                n =list2.index(strs)
                min_sum = min(min_sum, (n+i))
                res.append([i+n, strs])
        arr = []
        for idx, strs in res:
            if idx <= min_sum:
                arr.append(strs)
        return arr




        
            