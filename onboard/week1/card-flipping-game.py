class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        set_ele = set(fronts + backs)

        for i in range(len(fronts)):
            if fronts[i] == backs[i] and fronts[i] in set_ele:

                set_ele.remove(fronts[i])

        if len(set_ele) == 0:
            return 0
        else:
            return set_ele.pop()