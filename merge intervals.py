class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals)<2:return intervals


        start=intervals[0][0]
        end=intervals[0][1]
        output=[]
        for first,second in intervals[1:]:
            if end >= first:
                end = max(second,end)
            else:
                output.append([start,end])
                start=first
                end=second
        output.append([start,end])
        return output
