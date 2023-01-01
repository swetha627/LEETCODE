class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            if i.isalpha():
               res+=i.lower()
            if i.isnumeric():
                res+=i

        return res==res[::-1]
