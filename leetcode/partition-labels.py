class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #know the ending part of the character by updating dictt with their index
        dictt = {}
        for i in range(len(s)):
            dictt[s[i]] = i
        
        ar = []
        maxx = -1
        for i in range(len(s)):
            # check maxx is less than dictt of character and update max by equalizing with index
            if maxx < dictt[s[i]]:
                maxx = dictt[s[i]]
            # if its equal already know the ending of the character so,we get the partition
            if i == maxx:
               #print(maxx)
                ar.append(i+1)
        for i in range(len(ar)-1,0,-1):
            # update the last solution by substracting the current element with the previous one
            ar[i]=ar[i]-ar[i-1]
        return ar
        
        