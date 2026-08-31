class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern)!=len(words):
            return False
        p_w ={}
        w_p = {}
        for i in range(len(pattern)):
            p=pattern[i]
            w=words[i]
            if p in p_w and p_w[p]!=w:
                return False
            if w in w_p and w_p[w]!=p:
                return False
            p_w[p] = w
            w_p[w] = p

        return True