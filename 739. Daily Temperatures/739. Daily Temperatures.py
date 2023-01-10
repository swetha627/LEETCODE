#https://leetcode.com/problems/daily-temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #using stack
        stack=[] #[temperature, index]
        ans=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                ans[stackIndex]=i-stackIndex
            stack.append([t,i])
        return ans
        
        
        
        # BRUTE FORCE
        # ans=[]
        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             ans.append(j-i)
        #             break
        #     else:
        #         ans.append(0)
        # return ans
