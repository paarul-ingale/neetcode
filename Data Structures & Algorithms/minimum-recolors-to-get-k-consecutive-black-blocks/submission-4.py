class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        curr_whites = 0
        min_whites = len(blocks)

        for right in range(len(blocks)):

            if blocks[right] == 'W':
                curr_whites += 1
            if right - left + 1 > k:
                if blocks[left] == 'W':
                    curr_whites -= 1
                left += 1
            if right - left + 1 == k:
                min_whites = min(min_whites, curr_whites)

        return min_whites