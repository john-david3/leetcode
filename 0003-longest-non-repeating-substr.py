class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = max_len = 0
        prev_dup = -1
        h_map = {}
        for i in range(len(s)):
            if s[i] not in h_map:
                h_map[s[i]] = i
                curr += 1
                if curr > max_len:
                    max_len = curr
            else:
                prev_pos = h_map[s[i]]
                if prev_pos > prev_dup:
                    curr = i - prev_pos
                else:
                    curr += 1
                    if curr > max_len:
                        max_len = curr
                if prev_pos > prev_dup:
                    prev_dup = prev_pos
                h_map[s[i]] = i
        return max_len
    
sol = Solution()
print(sol.lengthOfLongestSubstring("tmmzuxt"))
