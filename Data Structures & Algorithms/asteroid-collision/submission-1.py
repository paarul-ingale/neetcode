class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for current in asteroids:
            if not stack:
                stack.append(current)
            else:
                top = stack[-1]
                alive = True
                while stack and top > 0 and current < 0:
                    if abs(top) < abs(current):
                        stack.pop()
                        alive  = True
                    elif abs(current)< abs(top):
                        alive = False
                        break
                    else:
                        stack.pop()
                        alive = False
                        break
                    
                    if stack:
                        top = stack[-1]   
                if alive==True: 
                    stack.append(current)
        return stack 