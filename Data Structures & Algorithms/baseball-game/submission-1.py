class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        add = 0
        for ch in operations:
            
            if ch =='C':
                    score = stack.pop()
                    add -= score
            elif ch =='D':
                    score = stack[-1] * 2
                    add+=score
                    stack.append(score)

            
            elif ch == '+':
                    score = stack[-1] + stack[-2]
                    stack.append(score)
                    add += score

            else :
                stack.append(int(ch))
                add+=int(ch)
        return add