class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        ans = -1
        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i], 0) + 1 
        for f in freq:
            if f == freq[f]:
                ans = max(ans,f)
        return ans
