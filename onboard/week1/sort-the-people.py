class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        di = defaultdict(int)
        for i,num in enumerate(heights):
            di[num] = names[i]

        count_sort = [0]*(max(heights)+1)
        arr = []
        for num in heights:
            count_sort[num] = num

        for num in count_sort:
            if num in di:
               
                arr.append(di[num])

        return reversed(arr)

        