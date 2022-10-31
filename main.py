import pygame

from node import BLACK, WHITE, Grid, Node, NodeType

#Set display dimensions
DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 400

# Sets constants for display of grid
GRID_START_POS = (20, 20)
CELL_SIZE = 30


def main():
    # Sets up pygame
    pygame.init()
    game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("A* Pathfinding")
    game_display.fill(WHITE)

    # Initialises all grid varibles
    grid = Grid()
    draw_grid(game_display, grid.grid)

    # Creates list of open and closed nodes
    open = [] # Nodes on that are still a possibiliity 
    closed = [] # Nodes that have been checked and are not possible

    # Initialise the start point as a Node object, calculate its f cost, and add it to the open list
    start_node = Node(grid, grid.start_pos, NodeType.START)
    start_node.calc_f_cost()
    open.append(start_node)
    update_cell_display(game_display, start_node)

    run = True
    finished = False

    while run:
        
        # Quit case
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if not finished:
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
            
            # Generate the neighbour nodes of the current node
            current_node.get_neighbour_nodes(grid)

            for neighbour in current_node.neighbour_nodes:
                # If the neighbour is a wall or in the closed list skip it
                if grid.grid[neighbour.pos[0]][neighbour.pos[1]] == NodeType.WALL or neighbour in closed:
                    continue
                
                if neighbour.pos != start_node.pos:
                    neighbour.type = NodeType.CHECKED
                    update_cell_display(game_display, neighbour)

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

            # If current node is the end node, fill in completed grid with path
            if current_node.pos == grid.end_pos:
                path_node = current_node
                while path_node.parent is not None:  
                    pos = (path_node.parent.pos[0], path_node.parent.pos[1])
                    path_node.type = NodeType.PATH
                    update_cell_display(game_display, path_node)
                    path_node = path_node.parent
                    if pos == start_node.pos:
                        break
                finished = True



def update_cell_display(display, node: Node):
    """
        Change the colour of a cell at a given position.

        Parameters
            display: pygame display object 
            node: Node representing the cell that needs to be changed
    """
    cell_x = GRID_START_POS[0] + (node.pos[0] * CELL_SIZE) + 1
    cell_y = GRID_START_POS[1] + (node.pos[1] * CELL_SIZE) + 1
    if node.type == NodeType.PATH:
        print(node.pos[0], node.pos[1], node.type.value)
    pygame.draw.rect(display, node.type.value, (cell_y, cell_x, CELL_SIZE - 2, CELL_SIZE - 2), 0)
    pygame.display.update()
    pygame.time.delay(5)


def draw_grid(display, grid):
    """
        Draw a grid to the Pygame display

        Parameters
            display: Pygame display object 
            grid: Nestesd lists that represent a 12x12 grid of ints 
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            cell = grid[row][col]

            cell_fill = 0 if cell != NodeType.EMPTY else 1
            cell_colour = cell.value if cell != NodeType.EMPTY else BLACK

            cell_start_x = GRID_START_POS[0] + (row * CELL_SIZE)
            cell_start_y = GRID_START_POS[1] + (col * CELL_SIZE)
            pygame.draw.rect(display, cell_colour, (cell_start_y, cell_start_x, CELL_SIZE, CELL_SIZE), cell_fill)
            

    pygame.display.update()


if __name__ == "__main__":
    main()
