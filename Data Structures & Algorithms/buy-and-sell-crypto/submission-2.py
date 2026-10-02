class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = 1
        maxProfit = 0
        while r < n:
            if prices[r] < prices[l]:
                l = r
                # r += 1
            maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1
        return maxProfit