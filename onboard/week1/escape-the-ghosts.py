class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        for i in range(len(ghosts)):
            for j in range(1):
                
                if abs(ghosts[i][0]-target[0]) + abs(ghosts[i][1] -target[1]) <= abs(target[0]) + abs(target[1]):
                    return False
        return True

        