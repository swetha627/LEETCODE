class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i%2==0:
                d[i]=d.get(i, 0)+1
        maxx=0
        output = -1        
        for k,v in d.items():
            if v > maxx:
                maxx, output = v,k
            elif v == maxx:
                output = min(k,output)
        return output
        