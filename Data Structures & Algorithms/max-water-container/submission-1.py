class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        maxArea = 0
        while l < r:
            if heights[l] <= heights[r]:
                area = heights[l] * (r - l)
                l += 1
            elif heights[l] > heights[r]:
                area = heights[r] * (r - l)
                r -= 1
            maxArea = max(area, maxArea)
        return maxArea