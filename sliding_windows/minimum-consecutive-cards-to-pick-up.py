class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l = 0
        res = float('inf')
        d = defaultdict(int)
        for i in range(len(cards)):
            while cards[i] in d:
                
                if cards[l] == cards[i]:
                    res = min(res,i-l+1)
                    
                d[cards[l]] -=1
                if d[cards[l]]==0:
                    del d[cards[l]]

                l += 1

            d[cards[i]] += 1
        return res if res!=float('inf') else -1
        