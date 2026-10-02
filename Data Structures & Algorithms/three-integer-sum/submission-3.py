class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans=[]
        for i in range(n-2):
            if i > 0 and nums[i-1]==nums[i] :
                continue
            l = i + 1
            r = n - 1
            target = -1 * nums[i]
            while l < r:
                if nums[l] + nums[r] < target:
                    l+=1
                elif nums[l] + nums[r] > target:
                    r-=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    while(l < r and nums[l]==nums[l+1]):
                        l+=1
                    while (l < r and nums[r]==nums[r-1]):
                        r-=1
                    l+=1
                    r-=1
        return ans
                    

            