class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #approach1: simple just maintain a set and grow untill found in seen. shrink untill right end is not in seen .

        seen = set()
        l=r=0
        ans=0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                ans= max(ans,r-l+1)
                r+=1
            else:
                while s[r] in seen and l<r:
                    seen.remove(s[l])
                    l+=1
        return ans