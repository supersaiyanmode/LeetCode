from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.hours_map = defaultdict(list)
        self.minutes_map = defaultdict(list)
        
        for h in range(12):
            self.hours_map[self.bit_count(h)].append(str(h))
        for m in range(60):
            self.minutes_map[self.bit_count(m)].append("%02d"%m)
    
    def bit_count(self, num):
        count = 0
        while num:
            num = num & (num - 1)
            count += 1
        return count

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        for i in range(num+1):
            hours, minutes = i, num - i
            result += [x + ":" + y for x in self.hours(hours) for y in self.minutes(minutes)]
        return result
    
    def hours(self, num):
        return self.hours_map[num]
    
    def minutes(self, num):
        return self.minutes_map[num]
        
        
        
        