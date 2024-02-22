class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        counter = i = 0
        idx = 0
        while tickets[k]!=0:
            if tickets[idx] != 0:
                counter += 1
                tickets[idx] -= 1
            i += 1
            idx = i%n
     
        return counter
