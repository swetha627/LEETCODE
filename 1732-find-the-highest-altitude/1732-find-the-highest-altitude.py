class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=[0]
        val=0
        res.append(gain[0])
        for i in range(1,len(gain)):
            val=res[i]+gain[i]
            res.append(val)
        return max(res)
