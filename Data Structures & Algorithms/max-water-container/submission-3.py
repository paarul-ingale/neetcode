class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        i = 0
        j = len(heights)-1
        while j-i != -1 :
            if max_vol < ((j-i)*min(heights[i],heights[j])):
                max_vol = ((j-i)*min(heights[i],heights[j]))
            if heights[i]>heights[j] :
                j-=1
            else :
                i +=1
        return max_vol