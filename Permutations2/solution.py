class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        return list(self.gen(nums))
        
    def gen(self, nums, level=0):
        if len(nums) == 1:
            yield nums
        seen_nums = set()
        for index, num in enumerate(nums):
            if num in seen_nums:
                continue
            seen_nums.add(num)
            remaining = [x for i,x in enumerate(nums) if i != index]
            for res in self.gen(remaining, level=level+1):
                yield [num] + res
