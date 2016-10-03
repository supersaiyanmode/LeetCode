class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        sieve = [True]*n
        false = [False]*n
        sieve[4:n:2] = false[4:n:2]
        sieve[6:n:3] = false[6:n:3]
        cur = 5
        while cur < n:
            if sieve[cur]:
                sieve[cur*2:n:cur] = false[cur*2:n:cur]
            cur += 2
        return sum(1 for x in sieve if x) - 2