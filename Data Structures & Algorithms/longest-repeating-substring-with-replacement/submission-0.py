class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_length = 0
        curr_len = 0
        left = 0
        for right in range (0,len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(freq.values())
            buffer = (right - left + 1) - max_freq
            if buffer<=k:
                curr_len+=1
            else:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left+=1
            max_length=max(max_length ,curr_len)   
        return max_length