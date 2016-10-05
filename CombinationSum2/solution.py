class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return list(self.proc(candidates, target, [], set()))
        
    def proc(self, available, target, used, cache):
        if target == 0:
            cache.add(tuple(used))
            yield used
        for i, x in enumerate(available):
            if target == x:
                if tuple(used + [x]) in cache:
                    continue
            if target >= x:
                rem = available[i+1:]
                for item in self.proc(rem, target - x, used + [x], cache):
                    if item:
                        yield item