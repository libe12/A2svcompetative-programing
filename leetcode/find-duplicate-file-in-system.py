class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        #["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
        c = defaultdict(list)

        for path in paths:
            path = path.split(' ')
            folder = path[0]

            for p in path[1:]:
                s = p.split('.txt')
                name = s[0]
                content = s[1]

                c[content].append((folder,name))
        output = []
        for key,val in c.items():
            if len(val) > 1:
                tmp = []
                for path,name in val:
                    tmp.append(path+'/'+name+'.txt')
                output.append(tmp)
            
        return output

        