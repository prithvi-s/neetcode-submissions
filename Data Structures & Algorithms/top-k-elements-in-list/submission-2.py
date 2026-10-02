class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        n = len(nums) + 1
        ans = [[] for _ in range(n)]

        for key, value in d.items():
            ans[value].append(key)
        finans=[]
        for i in range(len(ans) - 1, -1, -1):
            for num in ans[i]:
                finans.append(num)
                if len(finans) == k:
                    return finans
        return finans