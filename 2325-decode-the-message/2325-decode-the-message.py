class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d=dict()
        c=ord('a')
        for i in key:
            if i not in d and i!=" ":
                d[i]=chr(c)
                c+=1
        d[" "]=" "
        str=""
        for i in message:
            str+=d[i]
        return str


            
        
        