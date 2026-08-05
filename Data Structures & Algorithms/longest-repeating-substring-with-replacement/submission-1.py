class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_length = 0
        max_freq = 0
        left = 0
        for right in range (0,len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])
            buffer = (right - left + 1) - max_freq

            if buffer>k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left+=1
            max_length=max(max_length ,(right - left + 1))   
        return max_length