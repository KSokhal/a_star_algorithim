import math
from enum import Enum
from typing import Tuple

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0 , 255)
DARK_GREY = (65, 65, 65)

class NodeType(Enum):
    START = GREEN
    END = DARK_GREY
    WALL = BLACK
    EMPTY = WHITE
    CHECKED = RED
    PATH = BLUE

NODE_TYPE_DICT = {
    "S": NodeType.START,
    "E": NodeType.END,
    "W": NodeType.WALL,
    "O": NodeType.EMPTY,
}

class Grid:
    """Class to store data about the grid"""

    def __init__(self):
        self.grid_size = 12
        self.grid = self._get_grid()
        self.start_pos = None
        self.end_pos = None

        self._set_init_positions()
        

    def _get_grid(self):
        """Reads grid from text file."""
        grid = []
        with open("grid.txt") as file:
            for line in file.readlines():
                row = []
                line = line.strip()
                assert(len(line) == 12, "All rows must be contain 12 cells") 
                for letter in line:
                    assert(letter in NODE_TYPE_DICT, f"Unrecognized character in grid: {letter}" ) 
                    row.append(NODE_TYPE_DICT[letter])
                grid.append(row)
        assert(len(grid) == 12, "Grid must contain 12 rows") 
        return grid


    def _set_init_positions(self):
        """Get initial start and end positions from grid"""
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == NodeType.START:
                    self.start_pos = (row, col)
                elif self.grid[row][col] == NodeType.END:
                    self.end_pos = (row, col)
        if self.start_pos is None or self.end_pos is None:
            raise ValueError("Grid must contain both a start and end cell.")
        

class Node:
    """Class to represent a cell in the grid."""

    def __init__(self, Grid: Grid, pos: Tuple[int], type: NodeType, parent: 'Node' = None):
        self.pos = pos
        self.type = type
        self.g_cost = self.get_distance(Grid.start_pos) # Distance from starting node
        self.h_cost = self.get_distance(Grid.end_pos) # Distance from end node
        if parent:
            self.parent = parent
        else:
            self.parent = None
        

    def get_distance(self, reference_pos: Tuple[int]):
        """Get absolute distance from a postion on the grid."""
        dx = abs(self.pos[0] - reference_pos[0])
        dy = abs(self.pos[1] - reference_pos[1])
        return (abs(dx-dy) * 1) + (min(dx, dy) * math.sqrt(2))

    def calc_f_cost(self):
        """Calculate the f cost of the current node."""
        self.f_cost = self.g_cost + self.h_cost

    def get_neighbour_nodes(self, Grid):
        """Create the node objects for the cell that are around the current cell."""
        self.neighbour_nodes = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                else:
                    next_pos = (self.pos[0] + dx, self.pos[1] + dy)
                    next_node = Node(Grid, next_pos, NodeType.EMPTY)
                    self.neighbour_nodes.append(next_node)
