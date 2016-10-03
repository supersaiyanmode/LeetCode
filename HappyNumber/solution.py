class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.cache = {}
        return bool(self.calc(n))
        
    def calc(self, n):
        if n in self.cache:
            if self.cache[n] == -1:
                self.cache[n] = 0
                return 0
            return self.cache[n]
        if n == 1:
            return 1
        res = 0
        bkp = n
        while n:
            res += (n%10)**2
            n = n / 10
        self.cache[bkp] = -1
        res = self.calc(res)
        self.cache[bkp] = res
        return res
    
    