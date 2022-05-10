# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:24:39 2021

@author: atana
"""

import numpy as np

class Agent:
    
    def __init__(self, starting_position, grid, gamma):
        self.position = starting_position
        self.states = []
        self.R_states = []
        self.S_states = []
        for i in range(len(grid)-1):
            for j in range(len(grid)-1):
                if grid[i, j] == ' ':
                    self.states.append([i, j])
                else:
                    if grid[i, j] == 'R':
                        self.R_states.append([i, j])
                    else:
                        if grid[i, j] == 'S':
                            self.S_states.append([i, j])
                        else:
                            continue
        self.gamma = gamma
        self.grid_size = len(grid)
        self.action_probability = {"N" : 0.166,
                                   "E" : 0.166,
                                   "S" : 0.166,
                                   "W" : 0.166,
                                   "NE" : 0.083,
                                   "NW" : 0.083,
                                   "SE" : 0.083,
                                   "SW" : 0.083}
        self.special_case_probability = {"N" : 0.2,
                                         "E" : 0.1143,
                                         "S" : 0.1143,
                                         "W" : 0.1143,
                                         "NE" : 0.1143,
                                         "NW" : 0.1143,
                                         "SE" : 0.1143,
                                         "SW" : 0.1143}
        self.actions = list(self.action_probability.keys())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        