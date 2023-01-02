#https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res=[words[0]]
        for i in range(1, len(words)):
            if Counter(words[i-1])!=Counter(words[i]):
                res.append(words[i])
        return res

        
