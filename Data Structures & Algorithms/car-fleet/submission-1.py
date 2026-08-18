class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        time = {}
        for i in range(len(speed)): 

            dist = target - position[i]
            time[position[i]] = dist/speed[i]
        time = dict(sorted(time.items(), reverse=True))

        for position in time:
            t = time[position]
            if not stack or t>stack[-1]:
                stack.append(t)

        return len(stack)

            