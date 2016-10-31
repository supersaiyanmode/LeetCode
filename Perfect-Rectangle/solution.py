from collections import defaultdict

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        min_left, min_bottom = 10**10, 10**10
        max_right, max_top = 0, 0
        points = defaultdict(int)
        total_area = 0
        for rect in rectangles:
            points[(rect[0], rect[1])] += 1
            points[(rect[2], rect[3])] += 1
            points[(rect[0], rect[3])] += 1
            points[(rect[2], rect[1])] += 1
            
            min_left = min(min_left, rect[1])
            min_bottom = min(min_bottom, rect[0])
            max_right = max(max_right, rect[3])
            max_top = max(max_top, rect[2])
            cur_area = abs(rect[3] - rect[1]) * abs(rect[2] - rect[0])
            total_area += cur_area
        
        if total_area != (max_right - min_left) * (max_top - min_bottom):
            return False
        points[(min_bottom, min_left)] += 1
        points[(max_top, max_right)] += 1
        points[(min_bottom, max_right)] += 1
        points[(max_top, min_left)] += 1
        
        #print "\n".join(str(x) + " => " + str(y) for x,y in points.items())
        if any(x%2 for x in points.values()):
            return False
        return True
