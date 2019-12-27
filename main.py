
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

    start_pos = None
    end_pos = None

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "S":
                start_pos = (row, col)
            elif grid[row][col] == "E":
                end_pos = (row, col)

def get_scores(start_pos, end_pos, pos):
    g_cost = 0 # Distance from starting node
    h_cost = 0 # Distance from end node
    f_cost = 0 # g cost + h cost
    
    g_cost = ((pos[0] - start_pos[0])^2 + (pos[1] - start_pos[1])^2)^0.5
    h_cost = ((pos[0] - end_pos[0])^2 + (pos[1] - end_pos[1])^2)^0.5
    f_cost = g_cost + h_cost

    return g_cost, h_cost, f_cost






if __name__ == "__main__":
    main()