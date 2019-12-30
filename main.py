from node import Grid
from node import Node 
from copy import deepcopy

def main():

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
    complete_grid = deepcopy(grid)
    grid = Grid(grid)

    open = []
    closed = []

    start_node = Node(grid, grid.start_pos)
    start_node.calc_f_cost()
    open.append(start_node)
    current_node = start_node
    while True:
        current_node = open[0]
        for node in open:
            if node.f_cost == current_node.f_cost:
                if node.h_cost < current_node.h_cost:
                    current_node = node
            if node.f_cost < current_node.f_cost:
                current_node = node
        
        open.remove(current_node)
        closed.append(current_node)


        if current_node.pos == grid.end_pos:
            path_node = current_node
            while path_node.parent is not None:  
                pos = (path_node.parent.pos[0], path_node.parent.pos[1])
                if complete_grid[pos[0]][pos[1]] == "S":
                    break
                complete_grid[pos[0]][pos[1]] = "P"
                path_node = path_node.parent

            break
        
        neighbour_nodes = get_neighbour_nodes(grid, current_node)

        for neighbour in neighbour_nodes:
            if grid.grid[neighbour.pos[0]][neighbour.pos[1]] == "W" or check_in(closed, neighbour):
                continue


            new_g_cost = current_node.g_cost + current_node.get_distance(current_node.pos,  neighbour.pos)

            if new_g_cost < current_node.g_cost or not check_in(open, neighbour):
                neighbour.g_cost = new_g_cost
                neighbour.h_cost = neighbour.get_distance(neighbour.pos, grid.end_pos)
                neighbour.calc_f_cost()
                neighbour.parent = current_node
                if not check_in(open, neighbour):
                    open.append(neighbour)

        print(current_node.pos)
    print("found!")

    for i in complete_grid:
        print(i)

def check_in(lst, node):
    for n in lst:
        if n.pos == node.pos:
            return True
    return False

def get_neighbour_nodes(grid, node):
    neighbour_nodes = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            else:
                pos = (node.pos[0] + dx, node.pos[1] + dy)
                next_node = Node(grid, pos)
                neighbour_nodes.append(next_node)



    return neighbour_nodes







if __name__ == "__main__":
    main()