class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        count=0
        se=sorted(seats)
        st=sorted(students)
        for i in range(len(se)):
            count+=abs(se[i]-st[i])
        return count
        