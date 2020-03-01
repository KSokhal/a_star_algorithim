from node import Grid, Node
from copy import deepcopy

import pygame

#Set display dimensions
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600

# Sets colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0 , 255)
LIGHT_GREY = (100, 100, 100)
DARK_GREY = (65, 65, 65)

# Sets constants for display of grid
GRID_START_POS = (10, 10)
CELL_SIZE = 30

COLOURS = {
            "S": LIGHT_GREY,
            "E": DARK_GREY, 
            "W": BLACK
          }

def main():

    # Sets up pygame
    pygame.init()
    game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("A* Pathfinding")
    game_display.fill(WHITE)
    clock = pygame.time.Clock()

    # Initialises all grid varibles
    grid = Grid()
    draw_grid(game_display, grid.grid)
    # Creates copy of grid to fill in after path found
    complete_grid = deepcopy(grid.grid)

    # Creates list of open and closed nodes
    open = [] # Nodes on that are still a possibiliity 
    closed = [] # Nodes that have been checked and are not possible

    # Initialise the start point as a Node object, calculate its f cost, and add it to the open list
    start_node = Node(grid, grid.start_pos, WHITE)
    start_node.calc_f_cost()
    open.append(start_node)
    change_colour(start_node.pos, GREEN, game_display)

    end = False

    while not end:

        # Quit case
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        # Set current node to first in open list
        current_node = open[0]
        

        # Search the open list for the node with the lowest f cost and set it as the current node
        for node in open:
            if node.f_cost == current_node.f_cost:
                if node.h_cost < current_node.h_cost:
                    current_node = node
            if node.f_cost < current_node.f_cost:
                current_node = node


        # Remove node from the open list and add it to the closed list
        open.remove(current_node)
        closed.append(current_node)
        if current_node.colour != RED:
            change_colour(current_node.pos, GREEN, game_display)
            current_node.colour = GREEN

        # If current node is the end node, fill in completed grid with path
        if current_node.pos == grid.end_pos:
            path_node = current_node
            while path_node.parent is not None:  
                pos = (path_node.parent.pos[0], path_node.parent.pos[1])
                if complete_grid[pos[0]][pos[1]] == "S":
                    break
                change_colour(path_node.pos, BLUE, game_display)
                complete_grid[pos[0]][pos[1]] = "P"
                path_node = path_node.parent
            input("End?")
            break
        
        # Generate the neighbour nodes of the current node
        current_node.get_neighbour_nodes(grid)

        for neighbour in current_node.neighbour_nodes:
            

            # If the neighbour is a wall or in the closed list skip it
            if grid.grid[neighbour.pos[0]][neighbour.pos[1]] == "W" or neighbour in closed:
                continue
            
            change_colour(neighbour.pos, RED, game_display)
            neighbour.colour = RED

            # Calculate the new g cost
            new_g_cost = current_node.g_cost + current_node.get_distance(neighbour.pos)

            # If the new g cost is smaller than the old one or the node isn't in the open list, add it to the open list
            if new_g_cost < current_node.g_cost or neighbour not in open:
                neighbour.g_cost = new_g_cost
                neighbour.h_cost = neighbour.get_distance(grid.end_pos)
                neighbour.calc_f_cost()
                neighbour.parent = current_node
                if neighbour not in open:
                    open.append(neighbour)




def change_colour(pos, new_colour, game_display):
    pygame.draw.rect(game_display, new_colour, (GRID_START_POS[0] + (pos[0] * CELL_SIZE) + 1, GRID_START_POS[1] + (pos[1] * CELL_SIZE) + 1, CELL_SIZE - 2, CELL_SIZE - 2), 0)
    pygame.display.update()



## Draws a grid
#
# @param display, the pygame display
# @param grid, nestesd lists that represent a 9x9 grid of intergers

def draw_grid(display, grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            cell_value = grid[row][col]
            if cell_value in COLOURS:
                cell_colour = COLOURS[cell_value]
                cell_fill = 0
            else:
                cell_colour = BLACK
                cell_fill = 1

            pygame.draw.rect(display, cell_colour, (GRID_START_POS[0] + (row * CELL_SIZE), GRID_START_POS[1] + (col * CELL_SIZE), CELL_SIZE, CELL_SIZE), cell_fill)
            
    
    pygame.display.update()

def print_text_grid(grid):
    [print(i) for i in grid]
    print("\n")

if __name__ == "__main__":
    main()