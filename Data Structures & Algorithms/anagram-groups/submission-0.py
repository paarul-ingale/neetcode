class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = {}
        for word in strs:
            key = tuple(sorted(word))
            if key in new_dict:
                new_dict[key].append(word)
            else:
                new_dict[key]=[word]
        return list(new_dict.values())