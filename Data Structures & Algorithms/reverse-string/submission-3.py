class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        j=n-1
        for i in range (0 , n//2):
            s[i] , s[j] = s[j] , s[i]
            j-=1