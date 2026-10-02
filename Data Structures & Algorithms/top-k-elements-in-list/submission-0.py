class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1

        ans = []

        for key in sorted(d, key = d.get, reverse = True):
            if len(ans) < k:
                ans.append(key)
            else:
                break
        
        return ans

            