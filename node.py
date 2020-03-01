import math


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0 , 255)
LIGHT_GREY = (100, 100, 100)
DARK_GREY = (65, 65, 65)


class Grid:

    def __init__(self):
        self.grid = self.get_grid()
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == "S":
                    self.start_pos = (row, col)
                elif self.grid[row][col] == "E":
                    self.end_pos = (row, col)

    # Creats grid from text on notepad
    #
    # @return grid, nestesd lists that represent a 9x9 grid of intergers

    def get_grid(self):
        grid = []
        with open("grid.txt") as file:
            for line in file.readlines():
                row = []
                for letter in line.strip("\n"):
                    row.append(letter)
                grid.append(row)
        return grid


    # Prints grid in easier to see manor
    def print_text_grid(self):
        [print(i) for i in self.grid]
        print("\n")

class Node:

    def __init__(self, Grid, pos, colour, parent = None):
        self.pos = pos
        self.g_cost = self.get_distance(Grid.start_pos) # Distance from starting node
        self.h_cost = self.get_distance(Grid.end_pos) # Distance from end node
        if parent:
            self.parent = parent
        else:
            self.parent = None
        self.colour = colour
        

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
                    next_node = Node(Grid, next_pos, colour=WHITE)
                    self.neighbour_nodes.append(next_node)