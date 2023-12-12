class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mydiw=defaultdict(int)
        mydil=defaultdict(int)
        res1=[]
        res2=[]
        for win, loss in matches:
            mydiw[win]+=1
            mydil[loss]+=1
        for num in mydiw:
            if num not in mydil:
                res1.append(num)
        for num in mydil:
            if mydil[num]==1:
                res2.append(num)
        return [sorted(res1),sorted(res2)]