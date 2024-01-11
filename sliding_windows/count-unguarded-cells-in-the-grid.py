class Solution:
    def countUnguarded(self, r: int, c: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        grid = [[0]*c for _ in range(r)]

        used = 3
        guard = 1
        wall = 2
         
        for x,y in guards:
            grid[x][y] = 1
        for x,y in walls:
            grid[x][y] = 2
        
        for i in range(r):
            cur = 0
            for j in range(c):
                if grid[i][j]==guard:
                    cur = used
                elif grid[i][j]==wall:
                    cur = 0
                elif grid[i][j]==0:
                    if cur == used:
                        grid[i][j]='G'
                    
        for i in range(r):
            cur = 0
            for j in range(c-1,-1,-1):
                if grid[i][j]==guard:
                    cur = used
                elif grid[i][j]==wall:
                    cur = 0
                elif grid[i][j]==0:
                    if cur ==used:
                        grid[i][j]='G'
        for i in range(c):
            cur = 0
            for j in range(r):
                if grid[j][i]==guard:
                    cur = used
                elif grid[j][i]==wall:
                    cur = 0
                elif grid[j][i]==0:
                    if cur ==used:
                        grid[j][i]='G'
        for i in range(c):
            cur = 0
            for j in range(r-1,-1,-1):
                if grid[j][i]==guard:
                    cur = used
                elif grid[j][i]==wall:
                    cur = 0
                elif grid[j][i]==0:
                    if cur ==used:
                        grid[j][i]='G'
        print(grid)
       
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    count += 1
        return count


        
       


                
      