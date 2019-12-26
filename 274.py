class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        total_citation = len(citations)
        for i in range(total_citation):
            if citations[i] >= total_citation - 1:
                return total_citation - i
        return 0
