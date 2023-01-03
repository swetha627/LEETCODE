#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in numbers:
            if target-i in d:
                if (target-i) == i:
                    return [numbers.index(target-i)+1, numbers.index(i)+2]
                else:
                    return [numbers.index(target-i)+1, numbers.index(i)+1]
            d[i]=d.get(i, 0)+1
