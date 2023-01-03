#https://leetcode.com/problems/container-with-most-water/description
class Solution:
    def maxArea(self, height: List[int]) -> int:
    #   BRUTE FORCE

    #   MaxArea=0
    #    for i in range(len(height)):
    #       for j in range(i+1, len(height)):
    #           area=(j-i)*min(height[i], height[j])
    #          MaxArea=max(MaxArea, area)
    #  return MaxArea

    # TWO POINTER SOLUTION

        MaxArea=0
        left, right=0, len(height)-1
        while left<right:
            area=(right-left)*min(height[left], height[right])
            MaxArea=max(MaxArea, area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return MaxArea
