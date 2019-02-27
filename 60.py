class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        curr = []
        self.result = ''
        for i in range(1, n + 1):
            curr.append(i)
        self.getPermutationHelper(n, k, curr)
        return self.result

    def getPermutationHelper(self, index, rest, curr):

        if index == 0:
            return
        for i in range(index - 1, -1, -1):
            temp = math.factorial(index - 1)
            # print temp, i, rest - (temp * i + 1)
            if rest - (temp * i + 1) >= 0:
                self.result += str(curr[i])
                curr.pop(i)
                # print(curr)
                self.getPermutationHelper(index - 1, rest - (temp * i), curr)
                break
