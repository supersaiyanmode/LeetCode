class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        
        queue = [(start, 0)]
        seen = {start}
        while queue:
            front, path_len = queue.pop(0)
            #print " "*path_len, front
            if front == end:
                return path_len
            for index, c in enumerate(front):
                for c1 in "A T C G".split():
                    if c1 != c:
                        new_str = front[:index] + c1 + front[index+1:]
                        if new_str in bank and new_str not in seen:
                            queue.append((new_str, path_len+1))
                            seen.add(new_str)
        return -1
            