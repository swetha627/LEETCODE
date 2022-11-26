class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return (len([i for j,i in enumerate(sorted(heights)) if i!=heights[j] ]))
        