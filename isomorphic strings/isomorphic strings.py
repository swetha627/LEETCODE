# https://leetcode.com/problems/isomorphic-strings/description

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in d.values():
                    return False
                else:
                    d[s[i]]=t[i]
            else:
                if t[i]==d[s[i]]:
                    continue
                else:
                    return False
        return True
