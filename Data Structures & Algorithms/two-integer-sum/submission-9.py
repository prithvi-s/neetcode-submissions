class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target-nums[i]],i]
            d[nums[i]]=i
        return []

        # for i in range(len(nums)):
        #     if nums[i] not in d:
        #         d[nums[i]]=i
        #     elif nums[i]*2==target:
        #         return [d[nums[i]],i]

        # for i in range(len(nums)):
        #     diff = target-nums[i]
        #     if diff in d and i!=d[diff]:
        #         return [i,d[diff]]
        return []