class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step = 0
        res = capacity
        for i, num in enumerate(plants):
            if res - plants[i] < 0:
                res = capacity - plants[i]
                step += (2*i + 1)
            else:
                res -= plants[i]
                step += 1
        return step
            