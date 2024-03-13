class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda lst:lst[0]-lst[1])
        selected = []

        left, right = 0, len(costs)-1

        while left < right :
            selected.append(costs[left][0])
            selected.append(costs[right][1])

            left += 1
            right -= 1
        return sum(selected)

    
        