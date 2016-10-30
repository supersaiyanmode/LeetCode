dig_maps = {
    "1": "*",
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
}

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return ["".join(x) for x in self.proc(digits)]
    
    def proc(self, digits):
        print digits
        if len(digits) != 0:
            sub_res = self.proc(digits[1:])
            yielded = False
            for sub in sub_res:
                yielded = True
                for ch in dig_maps[digits[0]]:
                    yield [ch] + sub
            if not yielded:
                for ch in dig_maps[digits[0]]:
                    yield [ch]
            
            