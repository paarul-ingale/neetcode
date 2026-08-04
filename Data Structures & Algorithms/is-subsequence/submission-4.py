class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in range (len(t)):
            if len(s) == 0:
                return True

            if j < len(s) and s[j] == t[i]:
                j+=1
            
        if j == len(s) :
            return True
        
        else:
            return False