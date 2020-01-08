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
        self.g_cost = self.get_distance(Grid.start_pos) # Distance from starting node
        self.h_cost = self.get_distance(Grid.end_pos) # Distance from end node
        if parent:
            self.parent = parent
        else:
            self.parent = None

    def get_distance(self, reference_pos):
        dx = abs(self.pos[0] - reference_pos[0])
        dy = abs(self.pos[1] - reference_pos[1])
        return (abs(dx-dy) * 1) + (min(dx, dy) * math.sqrt(2))

    def calc_f_cost(self):
        self.f_cost = self.g_cost + self.h_cost

    def get_neighbour_nodes(self, Grid):
        self.neighbour_nodes = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                else:
                    next_pos = (self.pos[0] + dx, self.pos[1] + dy)
                    next_node = Node(Grid, next_pos)
                    self.neighbour_nodes.append(next_node)