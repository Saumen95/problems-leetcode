class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        if not intervals:
            return result
        intervals.sort(key=lambda x: x.start)
        result.append(intervals[0])
        for interval in intervals[1:]:
            prev = result[-1]
            if prev.end >= interval.start:
                prev.end = max(prev.end, interval.end)
            else:
                result.append(interval)
        return result
