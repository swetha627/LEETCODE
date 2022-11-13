class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        size=len(s)
        index=0
        stack=[]
        res=""
        while index<size:
            if s[index]=='(':
                stack.append(index)
            elif s[index]==')':
                index_remove=stack.pop()
                if not stack:
                    res+=s[index_remove+1:index]
            index+=1
        return res
            
        