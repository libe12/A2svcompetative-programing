class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 ='qwertyuiop'
        row2 ='asdfghjkl' 
        row3 = 'zxcvbnm'
        max_len = max(len(word)for word in words)
        print(max_len)
        res = []
        counter1 = counter2 = counter3 = 0
        for i in range(len(words)):
            for j in range(max_len):
                if len(words[i])>j:
                    if words[i][j].upper() in row1 or words[i][j].lower() in row1 :
                        counter1 += 1
                    elif words[i][j].upper() in row2 or words[i][j].lower() in row2 :
                        counter2 += 1
                    elif words[i][j].upper() in row3 or words[i][j].lower() in row3 :
                        counter3 += 1

                    

                   
            if counter1 ==len(words[i]):
                res.append(words[i])
                counter1 = 0
            elif counter2 ==len(words[i]):
                res.append(words[i]) 
                counter2 = 0
            elif counter3 ==len(words[i]):
                res.append(words[i])
                counter3 = 0
            else:
                counter1 = counter2 = counter3 = 0
            
            
        return res


        