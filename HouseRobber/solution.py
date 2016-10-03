class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.proc(nums, 0, {})
    
    def proc(self, nums, start, cache):
        if start in cache:
            return cache[start]
        
        if start >= len(nums):
            return 0
        max_val = 0;
        for i, n in enumerate(nums[start:]):
            res = n + self.proc(nums, start + i + 2, cache)
            if res > max_val:
                max_val = res
        cache[start] = max_val
        return max_val