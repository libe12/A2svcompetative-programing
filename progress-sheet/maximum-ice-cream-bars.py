class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        arr = [0]*1000000
        d = Counter(costs)
        
        for cost in costs:
            arr[cost]=cost
        sorted_cost = []
        for cost in arr:
            if cost > 0:
                sorted_cost.append(cost)

        count = []
        for i,num in enumerate(sorted_cost):
            while d[num]!=0:
                
                count.append(num)
                d[num] -= 1
                
        res = 0
        canbuy =0
        for cost in count:
            if res + cost <=coins:
                res += cost
                canbuy += 1
            else:
                break
        return canbuy