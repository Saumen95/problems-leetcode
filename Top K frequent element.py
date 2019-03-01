class Solution(object):
    def topKFrequent(self, nums, k):
        """ :type nums: List[int] :type k: int :rtype: List[int] """
        frequencyMap = {}
        bucket = []
        for n in nums:
            if frequencyMap.get(n) != None:
                frequencyMap[n] += 1
            else:
                frequencyMap[n] = 1
            bucket.append([])
        bucket.append([])
        for item in frequencyMap:
            frequency = frequencyMap[item]
            bucket[frequency].append(item)
        res = []
        pos = len(bucket) - 1
        while pos >= 0 and len(res) < k:
            if len(bucket[pos]) > 0:
                for item in bucket[pos]:
                    res.append(item)
            pos -= 1
        return res
