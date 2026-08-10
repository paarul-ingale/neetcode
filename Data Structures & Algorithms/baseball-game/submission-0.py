class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        add = 0
        for ch in operations:
            if ch == 'C':
                score = stack.pop()
                add -= score
            elif ch == 'D':
                score = stack[-1] * 2
                stack.append(score)
                add += score
            elif ch == '+':
                score = stack[-1] + stack[-2]
                stack.append(score)
                add += score
            else:
                score = int(ch)
                stack.append(score)
                add += score

        return add   