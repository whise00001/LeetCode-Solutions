class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key=lambda x:x[0])

        for i in range(0,len(intervals)-1):
            if intervals[i][0] > intervals[i+1][0] or intervals[i][1] > intervals[i+1][1]:
                return False
        return True
            
