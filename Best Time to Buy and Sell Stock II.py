class Solution(object):

    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


if __name__ == '__main__':
print(Solution().maxProfit([3, 1, 5]))
