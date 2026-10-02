class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        maxLeftVal = height[0]
        maxRightVal = height[n - 1]
        for i in range(1, n):
            maxLeftVal = max(maxLeftVal,height[i - 1])
            maxLeft[i] = maxLeftVal
        print(maxLeft)
        for i in range(n - 2, -1, -1):
            maxRightVal = max(maxRightVal,height[i + 1])
            maxRight[i] = maxRightVal
        print(maxRight)
        waterUnit = 0
        finalWater = 0
        for i in range(n):
            waterUnit = (min(maxLeft[i], maxRight[i]) - height[i])
            if waterUnit > 0:
                finalWater += waterUnit 
        return finalWater
        