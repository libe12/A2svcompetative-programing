class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l=0
        space_add=[]
        for i, chars in enumerate(s):
            if spaces[-1] >= i:
                if i == spaces[l]:
                    space_add.append(' ')
                    l += 1
            space_add.append(chars)
        return ''.join(space_add)


        