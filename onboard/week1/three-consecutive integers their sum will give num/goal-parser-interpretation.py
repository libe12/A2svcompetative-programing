class Solution:
    def interpret(self, command: str) -> str:
        arr  = []
        if command[0]!='(':
            arr.append(command[0])
        for i in range(1, len(command)):
            if command[i]==')' and command[i-1]=='(':
                arr.append('o')
            elif command[i]!='(' and command[i]!=')':
                arr.append(command[i])

        return ''.join(arr)
            