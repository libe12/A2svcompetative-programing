class Solution:
    def intervalIntersection(self, fir: List[List[int]], sec: List[List[int]]) -> List[List[int]]:
        arr = []
        i = j = 0
        while i < len(fir) and j < len(sec):
            if fir[i][0] >= sec[j][0] and fir[i][1] <=sec[j][1]:
                arr.append([fir[i][0],fir[i][1]])
                i+=1
            elif sec[j][0] >=fir[i][0] and sec[j][1] <= fir[i][1]:
                arr.append([sec[j][0],sec[j][1]])
                j+=1
            elif  fir[i][0] >=sec[j][0] and fir[i][1] >=sec[j][1] and fir[i][0] <=sec[j][1]:
                arr.append([fir[i][0],sec[j][1]])
                j+=1
            elif fir[i][0] <=sec[j][0] and fir[i][1] <=sec[j][1] and fir[i][1] >=sec[j][0]:
                arr.append([sec[j][0],fir[i][1]])
                i+=1
            elif  fir[i][0] >=sec[j][0] and fir[i][1] >=sec[j][1] and fir[i][0] > sec[j][1]:
                j+=1
            elif fir[i][0] <=sec[j][0] and fir[i][1] <=sec[j][1] and fir[i][1] < sec[j][0]:
                i+=1
            else:
                i+=1
                j+=1
        return arr
            
        
        