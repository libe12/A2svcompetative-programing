class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ans = 0
        defd = defaultdict(int)
        for i,num in enumerate(bills):
            if num ==10:
                if not 5 in defd:
                    return False
                defd[5] -= 1
            if num == 20:
                if defd[10]>=1 and defd[5]>=1:
                    defd[10] -= 1
                    defd[5] -= 1
                elif defd[5] >=3:
                    defd[5] -= 3
                else:
                    return False
            defd[num] += 1
        return True
        