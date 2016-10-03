class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n % 4)
        results = [True, True, True, True, False]
        
        for i in range(5,n+1):
            if not results[i-1] or not results[i-2] or not results[i-3]:
                results.append(True)
            else:
                results.append(False)
        return results[n]
        