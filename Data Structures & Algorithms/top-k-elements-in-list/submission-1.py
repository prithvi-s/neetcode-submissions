class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        ans = []
        for key, value in sorted(d.items(),key=lambda item:item[1], reverse = True ):
            ans.append(key)
            k -= 1
            if k == 0:
                break
        return ans