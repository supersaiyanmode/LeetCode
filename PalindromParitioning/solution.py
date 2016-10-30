class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        if len(s) == 1:
            return [[s]]
        result = []
        for index, ch in enumerate(s):
            if s[:index+1] == s[:index+1][::-1]:
                sub_results = self.partition(s[index+1:])
                if not sub_results:
                    result.append([s[:index+1]])
                for sub_result in sub_results:
                    result.append([s[:index+1]] + sub_result)
        return result