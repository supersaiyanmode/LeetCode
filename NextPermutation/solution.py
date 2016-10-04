class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        found = False 
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                found = True
                break
        if not found:
            nums.reverse()
            return
        swap = min((j for j in range(i+1, len(nums)) if nums[j] > nums[i]), key=lambda x: nums[x])
        nums[swap], nums[i] = nums[i], nums[swap]
        nums[i+1:] = sorted(nums[i+1:])
        