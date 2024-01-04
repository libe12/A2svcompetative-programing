class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i = count = 0
        j = len(people)-1
        people.sort()


        while j >= i:
            if people[j] + people[i] <= limit:
                i+=1
                j-=1
                
            else:
                j-=1
            count += 1
            
        return count