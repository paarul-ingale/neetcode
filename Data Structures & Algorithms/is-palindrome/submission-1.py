class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  
       
        j = len(s)-1
        i=0
        while i < j:
            if s[i].isalnum():
                if s[j].isalnum():
                    if s[i] == s[j]:
                        i+=1                       
                    else:
                        return False
                        break
                j-=1
                continue
            i+=1
        return True  