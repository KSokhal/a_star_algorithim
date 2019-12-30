import math

class Grid:

    def __init__(self, grid):
        self.grid = grid
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "S":
                    self.start_pos = (row, col)
                elif grid[row][col] == "E":
                    self.end_pos = (row, col)



class Node:

    def __init__(self, Grid, pos, parent = None):
        self.pos = pos
        #self.g_cost = math.sqrt( ( (self.pos[0] - Grid.start_pos[0]) ** 2 + (self.pos[1] - Grid.start_pos[1]) ** 2 ))   # Distance from starting node
        #self.h_cost = math.sqrt( ( (Grid.end_pos[0]  - self.pos[0]) ** 2 + (Grid.end_pos[1] - self.pos[1] ) ** 2  ))   # Distance from end node
        self.g_cost = self.get_distance(self.pos, Grid.start_pos)
        self.h_cost = self.get_distance(self.pos, Grid.end_pos)
        if parent:
            self.parent = parent
        else:
            self.parent = None

    @staticmethod
    def get_distance(current_pos, reference_pos):
        dx = abs(current_pos[0] - reference_pos[0])
        dy = abs(current_pos[1] - reference_pos[1])
        return (abs(dx-dy) * 1) + (min(dx, dy) * math.sqrt(2))

    def calc_f_cost(self):
        self.f_cost = self.g_cost + self.h_cost