class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        result = 0
        prev_verticals = set()
        for row_num, row in enumerate(board):
            series_count = 0
            prev_ship = False
            verticals = set()
            for col_num, cell in enumerate(row):
                if cell == 'X':
                    prev_ship = True
                    series_count += 1
                else:
                    prev_ship = False
                    if series_count == 1:
                        verticals.add(col_num-1)
                    elif series_count > 1:
                        result += 1
                        print "Found ship at:", (row_num, col_num)
                    series_count = 0
            if series_count == 1:
                verticals.add(col_num)
            elif series_count > 1:
                        result += 1
                        print "Found ship at:", (row_num, col_num)
            print "Verticals:", verticals
            print "Found %s ships on row: %d"%(str(list(prev_verticals - verticals)), row_num)
            result += len(prev_verticals - verticals)
            prev_verticals = verticals
        return result + len(prev_verticals)
                    
                                
        