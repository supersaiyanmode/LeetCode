class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        hist_map = {}
        for s in strs:
            hist = self.get_hist(s)
            if hist in hist_map:
                hist_map[hist].append(s)
            else:
                res.append([s])
                hist_map[hist] = res[-1]
        return res
    
    def get_hist(self, string):
        hist = {}
        for x in string:
            if x in hist:
                hist[x] += 1
            else:
                hist[x] = 1
        return tuple(sorted(hist.items()))
                
        