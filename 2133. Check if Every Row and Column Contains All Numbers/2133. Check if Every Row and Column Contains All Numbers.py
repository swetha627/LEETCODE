#https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description/
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        n=len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] in rows[i] or matrix[i][j] in cols[j]:
                    return False
                rows[i].add(matrix[i][j])
                cols[j].add(matrix[i][j])
        return True
