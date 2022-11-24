class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            c=num.count(str(i))
            if c==int(num[i]):
                continue
            else:
                return False
        return True
            