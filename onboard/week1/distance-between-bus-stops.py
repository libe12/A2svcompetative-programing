class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        res1 = 0
        if start<=destination:
            res1 = sum(distance[start:destination])
        else:
            res1 = sum(distance[destination:start])
        res2 = sum(distance)-res1
        return min(res1,res2)
        
        