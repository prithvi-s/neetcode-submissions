class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n - 1

        while l < r:
            if numbers[r] + numbers[l] < target:
                l += 1
            elif numbers[r] + numbers[l] > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return [l + 1, r + 1]   
        # l = 0
        # r = l + 1

        # while r < n:
        #     if numbers[r] < target - numbers[l]:
        #         r += 1
        #     elif numbers[r] > target - numbers[l]:
        #         l += 1
        #     else:
        #         return [l + 1, r + 1]
        # return [l + 1, r + 1]     