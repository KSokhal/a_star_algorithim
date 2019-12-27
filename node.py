class Node:

    def __init__(pos, parent = None):
        self.pos = pos
        self.g_cost = 0 # Distance from starting node
        self.h_cost = 0 # Distance from end node
        self.f_cost = 0 # g cost + h cost
        if parent:
            self.parent = parent


    def get_costs(self, start_pos, end_pos):
        self.g_cost = ((self.pos[0] - start_pos[0])^2 + (self.pos[1] - start_pos[1])^2)^0.5
        self.h_cost = ((self.pos[0] - end_pos[0])^2 + (self.pos[1] - end_pos[1])^2)^0.5
        self.f_cost = g_cost + h_cost

