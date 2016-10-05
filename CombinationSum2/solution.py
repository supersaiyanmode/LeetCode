class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return list(self.proc(candidates, target, [], set()))
        
    def proc(self, available, target, used, cache):
        if target == 0:
            cache.add(tuple(used))
            yield used
        for i, x in enumerate(available):
            if used and x < used[-1]:
                continue
            if target == x:
                if tuple(used + [x]) in cache:
                    continue
            if target >= x:
                rem = [y for j, y in enumerate(available) if j != i]
                for item in self.proc(rem, target - x, used + [x], cache):
                    if item:
                        yield item
                    