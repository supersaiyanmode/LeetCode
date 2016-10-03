class Solution(object):
    def base3(self, num):
        ret = [num < 0]
        num = abs(num)
        while num:
            ret.append(num % 3)
            num = num / 3
        ret = ret + [0]*(31 - len(ret))
        return ret
        
    def to_int(self, base3):
        return sum(x * 3 ** index for index, x in enumerate(base3[1:])) * (1 - 2*base3[0])
        
    def add3(self, n1, n2):
        return [(x + y)%3 for x, y in zip(n1, n2)]
    
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0 for _ in range(32)]
        for num in nums:
            b3 = self.base3(num)
            res = self.add3(res, b3)
        return self.to_int(res)
        