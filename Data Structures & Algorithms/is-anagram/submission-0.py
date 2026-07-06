class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count={}
        t_count={}
        for alp in s:
            if alp in s_count:
                s_count[alp] += 1
            else:
                s_count[alp] =1
        for alp in t:
            if alp in t_count:
                t_count[alp] +=1
            else:
                t_count[alp] =1
        return s_count== t_count