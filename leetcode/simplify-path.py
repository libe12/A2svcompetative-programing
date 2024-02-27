class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        #path = p.split('/')
        for str in path.split('/'):
            #print(num)

        #for str in path:
            if str in ('','.'):
                continue
            if str == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(str)
       
        return '/' + '/'.join(stk)
        #print(path)