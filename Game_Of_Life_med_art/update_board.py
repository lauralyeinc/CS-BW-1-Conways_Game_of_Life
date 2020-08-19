def update_board(self):
    print (" Updating board ... ")
    # cells list for living cells to kill and cells to resurrent or keep alive
    goes_alive = []
    gets_killed = []

    for row in range(len(self._grid)):
        for column in range(len(self._grid[row])):

            #check neighbor pr. square
            check_neighbor = self.check_neighbor(row, column)

            living_neighbor_count = []

            for neighbor_cell in check_neighbor:
                #check live status of neighbor cell
                if neighbor_cell.is_alive():
                    living_neighbor_count.append(neighbor_cell)

            cell_object = self._grid[row][column]
            status_main_cell = cell_object.is_alive()

            # if cell is alive, check neighbor status
            if status_main_cell == True:
                if len(living_neighbor_count) < 2 or len(living_neighbor_count) > 3:
                    gets_killed.append(cell_object)

                if len(living_neighbor_count) == 3 or len(living_neighbor_count) == 2:
                    goes_alive.append(cell_object)
            
            else:
                if len(living_neighbor_count) == 3:
                    goes_alive.append(cell_object)
        
            #sett cell statuses
    for cell_items in goes_alive:
        cell_items.set_alive()

    for cell_items in gets_killed:
        cell_items.set_dead()
