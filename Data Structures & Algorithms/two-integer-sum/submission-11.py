class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x not in d:
                d[nums[i]] = i
            else:
                return [d[x],i]