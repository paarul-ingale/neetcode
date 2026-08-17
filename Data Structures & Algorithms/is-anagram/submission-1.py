class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_t={}
        d_s={}
        for ch in s:
            d_s[ch] = d_s.get(ch,0)+1
        for ch in t:
            d_t[ch] = d_t.get(ch,0)+1
        if d_s == d_t:
            return True
        else:
            return False
