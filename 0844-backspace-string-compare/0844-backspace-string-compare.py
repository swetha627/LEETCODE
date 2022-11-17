class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            ans=[]
            for i in string:
                if i!='#':
                    ans.append(i)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s)==build(t)            
                    
        