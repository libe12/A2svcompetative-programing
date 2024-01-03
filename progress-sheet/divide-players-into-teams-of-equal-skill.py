class Solution:
    def dividePlayers(self, skill: List[int]) -> int: 

        skill.sort()
        s = skill[0] + skill[-1]
        a = skill[0] * skill[-1]

        arr = []
        arr.append(a)

        l = 1
        r = len(skill)-2

        while r>l:
            if skill[r]+skill[l] == s:
                res = skill[r]*skill[l]
                arr.append(res)
            else:
                return -1
            r-=1
            l+=1
        return sum(arr)
        