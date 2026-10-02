class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        s = list(s)
        s.sort()
        count = 1
        longest = 0
        if len(s) == 0:
            return 0
        for i in range(len(s)-1):
            if s[i+1] == s[i] + 1:
                count+=1
            else:
                if count > longest : # 2, 3 , 4, 5, 10, 20 
                    longest = count # 0,1,2,3,4,5,6  -1,0
                count=1
        return max(count,longest)
