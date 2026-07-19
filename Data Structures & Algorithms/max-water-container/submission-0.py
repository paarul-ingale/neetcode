class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = []
        for i in range (0 , len(heights)):
            for j in range (0 , len(heights)):
                volume = min( heights[i] , heights[j]) * (j-i)
                vol.append(volume)
        return max(vol)
