from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        start = 0
        max_val = -1
        cur_set = defaultdict(int)
        index = 0
        while index < len(s):
            ch = s[index]
            if not cur_set[ch]:
                cur_set[ch] += 1
                max_val = max(max_val, index - start+1)
                index += 1
            else:
                cur_set[s[start]] -= 1
                start += 1
        return max_val
    
            