class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans=0
        for words in details:
            age= int(words[11])*10+int(words[12])
            if (age)>60:
                ans+=1
        return ans
