class Solution(object):
    def test(self, stones, cur_stone, prev_step, level=0):
        if not stones:
            return True
        if (cur_stone, prev_step) in self.cache:
            return self.cache[(cur_stone, prev_step)]
        for step in (prev_step - 1, prev_step, prev_step + 1):
            if step <= 0:
                continue
            if step + cur_stone in stones:
                res = self.test(stones[stones.index(step + cur_stone) + 1:], step+cur_stone, step, level+1)
                self.cache[(cur_stone, prev_step)] = res
                if res:
                    return res
        return False
        
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        self.cache = {}
        if stones[1] != 1:
            return False
        
        return self.test(stones[2:], stones[1], 1)