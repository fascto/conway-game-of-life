class Cell:
    def __init__(self, x_pos, y_pos, status=1):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.alive = status


    def check_neighbors(self, cell_state_map) -> int:

        neighbors = 0

        for x in range(self.x_pos-1, self.x_pos+1):
            for y in range(self.y_pos-1, self.y_pos+1): 
                if cell_state_map[x][y] == 1:
                    neighbors+=1
                else:
                    continue
        
        return neighbors

    def check_dead(self):
        pass

    def born():
        pass