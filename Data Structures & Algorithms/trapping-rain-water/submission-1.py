class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 0
        water =0
        i= 0
        j = len(height)-1
        while j - i>0:
            if height[i] < height[j]:
                if left <height[i]:
                    left = height[i]
                else:
                    water += left -height[i]
                i+=1
            else:
                if right<height[j]:
                    right = height[j]
                else:
                    water +=  right-height[j]
                j-=1
            
        return water