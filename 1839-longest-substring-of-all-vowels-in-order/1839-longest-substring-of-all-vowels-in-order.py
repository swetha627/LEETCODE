class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        d = {}
        d['a'] = {'a', 'e'}
        d['e'] = {'e', 'i'}
        d['i'] = {'i', 'o'}
        d['o'] = {'o', 'u'}
        d['u'] = {'u'}

        res, stack = 0, []
        for c in word: 
            if len(stack) == 0:
                if c == 'a':
                    stack.append(c)
                continue

            if c in d[stack[-1]]:
                stack.append(c)

                if c == 'u':
                    res = max(res, len(stack))

            else:
                if c != 'a':
                    stack = []
                else:
                    stack=['a']
        return res
        