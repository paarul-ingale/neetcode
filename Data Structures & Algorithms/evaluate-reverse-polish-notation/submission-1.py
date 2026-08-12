class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
                
            if tokens[i] in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if tokens[i] =='+':
                    stack.append(int(a)+int(b))
                elif tokens[i] =='-':
                    stack.append(int(a)-int(b))
                elif tokens[i] =='*':
                    stack.append(int(a)*int(b))
                else:
                    stack.append(int(int(a)/int(b)))
            else:
                stack.append(int(tokens[i]))
        ans = stack[-1] 

        return int(ans)