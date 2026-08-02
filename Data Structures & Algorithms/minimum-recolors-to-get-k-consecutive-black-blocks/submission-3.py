class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = len(blocks)
        curr_w = 0
        j = 0
        for i in range (0,len(blocks)):
            if i-j+1<=k:
                if blocks[i] == 'W':
                    curr_w +=1

            else:
                whites = min(whites , curr_w)
                if blocks[j] =='W':
                    curr_w -= 1
                j+=1

                if blocks[i] == 'W':
                    curr_w+=1
        whites = min(whites , curr_w)

        return whites