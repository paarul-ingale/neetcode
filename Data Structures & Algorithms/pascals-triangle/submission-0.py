class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        if numRows !=0:
            output.append([1])
            numRows-=1
        prev = [1,1]
        
        while numRows != 0:
            curr = []
            curr.append(1)
            for i in range(len(prev)-1):
                curr.append(prev[i]+prev[i+1])
            curr.append(1)
            output.append(prev)
            prev = curr
            numRows-=1
        
        return(output)
        