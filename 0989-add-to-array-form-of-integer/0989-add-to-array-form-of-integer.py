class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        temp=""
        for i in num:
            temp+=str(i)
        output=str(int(temp)+k)
        ans=[]
        for i in output:
            ans.append(int(i))
        return ans
        