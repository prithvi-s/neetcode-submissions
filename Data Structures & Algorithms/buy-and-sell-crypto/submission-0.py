class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = l + 1
        maxval = 0
        while(l < r and r < n):
            if prices[r] > prices[l]:
                maxval = max(maxval,prices[r] - prices[l])
            else:
                l = r
            r = r + 1
        return maxval
            

