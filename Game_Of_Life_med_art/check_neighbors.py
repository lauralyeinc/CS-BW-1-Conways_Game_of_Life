def check_neighbor(self, check_row, check_column):
    #how far are we searching
    search_min = -1 #left?
    search_max = 2 #right?

    #empty list to start, to add neighbors to.
    neighbor_list = []
    for row in range(search_min, search_max):
        for column in range(search_min, search_max):
            neighbor_row = check_row + row
            neighbor_column = check_column + column

            valid_neighbor = True

            if (neighbor_row) == check_row and (neighbor_column) == check_column:
                valid_neighbor = False
            
            if (neighbor_row) < 0 or (neighbor_row) >= self._columns:
                valid_neighbor = False
            
            if valid_neighbor:
                neighbor_list.append(self._grid[neighbor_row][neighbor_column])
                
    return neighbor_list  