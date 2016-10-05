def larger_counts(arr):
    """Returns a cumulative histogram, assuming arr is
    reverse sorted.
    """
    larger_count = [(arr[0], 1)]
    max_count = -1
    for item in arr[1:]:
        if larger_count[-1][0] != item:
            larger_count.append((item, larger_count[-1][1] + 1))
        else:
            larger_count[-1] = (larger_count[-1][0], larger_count[-1][1] + 1)
    return larger_count
def calc_gq(arr):
    """
    Assuming the latest conditions sent across by Debasis
    """
    #print arr
    arr.sort()
    larger_count = larger_counts(arr[::-1])
    ptr = 0
    gq = len(arr)
    while gq > 0:
        #print "Checking:", gq
        while ptr + 1 < len(larger_count) and larger_count[ptr + 1][0] >= gq:
            ptr = ptr + 1
            #print "Latest update:", larger_count[ptr]
        if gq <= larger_count[ptr][1] and gq <= larger_count[ptr][0]:
            #print "Found:", gq, larger_count[ptr]
            return gq
        gq -= 1
    return 0

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        return calc_gq(citations)
