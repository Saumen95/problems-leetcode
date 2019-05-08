class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sum_even = sum(x for x in A if x % 2 == 0)
        result = []

        for val, i in queries:

            if A[i] % 2 == 0:
                sum_even -= A[i]
            A[i] += val
            if A[i] % 2 == 0:
                sum_even += A[i]

            result.append(sum_even)

        return result