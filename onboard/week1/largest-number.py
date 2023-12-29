class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def cmp(x,y):
            if int(x+y) < int(y+x):
                return 1
            else:
                return 0
        a = [str(i) for i in nums]
        a.sort(reverse=True)
        if a[0]=='0':
            return '0'


        for i in range(len(a)-1):
            j = i
            while (j >=0):
                if a[j+1] in a[j]:
                    if cmp(a[j],a[j+1]):
                        tmp = a[j+1]
                        a[j+1]=a[j]
                        a[j]=tmp
                    j-=1
                else:
                    break
        return ''.join(a)


