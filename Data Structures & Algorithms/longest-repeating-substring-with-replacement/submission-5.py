class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        n = len(s)
        if n <= 1:
            return n
        l = 0
        r = 0
        maxfreq = 0
        maxrep = 0
        maxwind = 0
        while r < n:
            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]] += 1
            maxrep = max(d[s[r]],maxrep)
            currwind = r - l + 1
            if currwind - maxrep <= k:
                maxfreq = max(maxfreq, currwind - maxrep)
                maxwind = max(currwind,maxwind)
            else:
                d[s[l]]-=1
                l+=1
            r+=1     
        return maxwind
            