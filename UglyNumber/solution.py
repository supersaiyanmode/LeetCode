class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num:
            return False
        if num == 1:
            return True
        for factor in (2,3,5):
            while abs(num)%factor == 0:
                num = num / factor
        return num == 1
        