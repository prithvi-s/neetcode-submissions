class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord('a')] += 1
            if tuple(count) not in d:
                d[tuple(count)]= []
            d[tuple(count)].append(i)
        ans = []
        for key, value in d.items():
            ans.append(value)

        return ans

        
