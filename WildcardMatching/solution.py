class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p = "*".join(x for x in p.split("*") if x)
        return self.partition(p, s)
        
    def partition(self, s, p, level=0):
        print " "*level, "Partition called with: p=" +p + ", s=" + s 
        parts = p.split("*")
        can_match = [x for x in parts if "?" not in x]
        if not can_match:
            return self.match(s, p, level=level+1)
            
        largest = max(can_match, key=len)
        
        if not largest:
            return self.match(s, p, level=level+1)
        
        string_splits = s.split(largest)
        pattern_splits = p.split(largest)
        
        if not string_splits:
            return False
            
        for i in range(len(string_splits)):
            for j in range(len(pattern_splits)):
                if not self.match(string_splits[i], pattern_splits[j], level=level+1):
                    continue
                res1 = self.partition(largest.join(string_splits[:i]), largest.join(pattern_splits[:j]), level=level+1)
                res2 = self.partition(largest.join(string_splits[i+1:]), largest.join(pattern_splits[j+1:]), level=level+1)
                if res1 and res2:
                    return True
        return False
                
        
    def match(self, s, p, level=0):
        print " "*level, "match called with: s="+s+" p="+p
        
        if not p and not s:
            return True
        if p == "*":
            return True
        if s and not p:
            return False
        if p and not s:
            return False
        if p[0] == '?':
            return self.match(s[1:], p[1:], level=level+1)
        elif p[0] == '*':
            for pos in range(0, len(s)):
                res = self.match(s[pos:], p[1:], level=level+1)
                if not res:
                    return True
            return False
        else:
            while p and s:
                print " "*level, "Processing with: s="+s+" p="+p
                if p[0] == '*':
                    return self.match(s, p, level=level+1)
                if p[0] != '?' and p[0] != s[0]:
                    return False
                p = p[1:]
                s = s[1:]
            return self.match(s, p, level=level+1)
            
            
        