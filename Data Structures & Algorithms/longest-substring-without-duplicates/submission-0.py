class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_set = set()
        l, r = 0, 0
        count,maxval=0, 0
        while(r < n):
            while(s[r] in char_set):
                char_set.remove(s[l])
                l+=1
                count-=1
            char_set.add(s[r])
            r+=1
            count+=1
            maxval = max(count,maxval)
        return maxval






        # d = {}
        # l = 0
        # r = 1
        # count = 1
        # if n <= 1:
        #     return n
        # if s[0] not in d:
        #     d[s[0]]=1
        # maxval = 1
        # while(l < r and r < n):
        #     if s[r] not in d:
        #         d[s[r]]=1
        #         count+=1
        #         r+=1
        #     else:
        #         while s[l] 
        #         d.pop(s[l])
        #         l+=1
        #         count-=1
        #     maxval = max(maxval, count)
        # return maxval

