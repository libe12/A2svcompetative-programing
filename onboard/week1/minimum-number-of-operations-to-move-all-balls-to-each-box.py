class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        res = []
        for i in range(len(boxes)):
            ind_dif=0
            for j in range(len(boxes)):
                if int(boxes[j])%2==1:
                    ind_dif +=abs(j-i)
            res.append(ind_dif)
        return res
        