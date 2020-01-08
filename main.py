from node import Grid
from node import Node 
from copy import deepcopy

def main():
    # Creates grid to path find for
    # S = Start point, E = End point, W = Walls
    grid =  [
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "S", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "W", "W", "W", "W", "O", "O", "O"],
            ["O", "O", "O", "O", "W", "W", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "W", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "E", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
            ]

    # Creates copy of grid to fill in after path found
    complete_grid = deepcopy(grid)
    # Creates grid object
    grid = Grid(grid)

    # Creates list of open and closed nodes
    open = [] # Nodes on that are still a possibiliity 
    closed = [] # Nodes that have been checked and are not possible

    # Initialise the start point as a Node object, calculate its f cost, and add it to the open list
    start_node = Node(grid, grid.start_pos)
    start_node.calc_f_cost()
    open.append(start_node)

    while True:
        # Set current node to first in open list
        current_node = open[0]

        # Search the open list for the node with the lowest f cost adn set it as the current node
        for node in open:
            if node.f_cost == current_node.f_cost:
                if node.h_cost < current_node.h_cost:
                    current_node = node
            if node.f_cost < current_node.f_cost:
                current_node = node
        
        # Remove node from the open list and add it to the closed list
        open.remove(current_node)
        closed.append(current_node)

        # If current node is the end node, fill in completed grid with path
        if current_node.pos == grid.end_pos:
            path_node = current_node
            while path_node.parent is not None:  
                pos = (path_node.parent.pos[0], path_node.parent.pos[1])
                if complete_grid[pos[0]][pos[1]] == "S":
                    break
                complete_grid[pos[0]][pos[1]] = "P"
                path_node = path_node.parent
            break
        
        # Generate the neighbour nodes of the current node
        current_node.get_neighbour_nodes(grid)

        for neighbour in current_node.neighbour_nodes:
            # If the neighbour is a wall or in the closed list skip it
            if grid.grid[neighbour.pos[0]][neighbour.pos[1]] == "W" or neighbour in closed:
                continue

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

    print("Completed!")

    for i in complete_grid:
        print(i)


if __name__ == "__main__":
    main()