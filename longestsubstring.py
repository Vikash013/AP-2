#sliding window and set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxl = 0
        _set = set()

        for r in range(len(s)):
            while s[r] in _set:
                _set.remove(s[l])
                l += 1
            
            _set.add(s[r])
            maxl = max(maxl, r-l+1)
        return maxl
