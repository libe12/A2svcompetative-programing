class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cur_num=''
        for r in range(2,len(num)):
            if num[r]==num[r-1] and num[r]==num[r-2]:

                if cur_num and int(num[r]) > int(cur_num[-1]):


                    cur_num=num[r-2:r+1]
                if not cur_num:
                    cur_num=num[r-2:r+1]
        return cur_num if cur_num else ""