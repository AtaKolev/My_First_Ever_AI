# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:24:39 2021

@author: atana
"""

import numpy as np

class Agent:
    
    def __init__(self, starting_position, grid, gamma,
                 treat, stick, learning_tolerance):
        self.position = starting_position
        self.grid = grid
        self.treat = treat
        self.stick = stick
        self.learning_tolerance = learning_tolerance
        self.states = []
        self.R_states = []
        self.S_states = []
        self.edges = []
        for i in range(self.grid.shape[0]-1):
            for j in range(self.grid.shape[1]-1):
                if grid[i, j] == ' ':
                    self.states.append((i, j))
                elif grid[i, j] == 'R':
                    self.R_states.append((i, j))
                elif grid[i, j] == 'S':
                    self.S_states.append((i, j))
                else:
                    self.edges.append((i, j))
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
        self.movements = {"N" : (1, 0),
                          "E" : (0, 1),
                          "W" : (0, -1),
                          "S" : (-1, 0),
                          "NE" : (1, 1),
                          "NW" : (1, -1),
                          "SE" : (-1, 1),
                          "SW" : (-1, -1)}
        
    def next_state_and_reward(self, state, action):
        
        next_state = tuple(sum(ele) for ele in zip(state, self.movements[action]))
        if next_state in self.edges:
            next_state = state
        
        if next_state in self.R_states:
            return next_state, self.treat
        elif next_state in self.S_states:
            return next_state, self.stick
        else:
            return next_state, 0
        
    def evaluate_state_values(self):
        
        new_state_values = np.zeros((self.grid.shape[0], self.grid.shape[1]))
        self.state_values = new_state_values.copy()
        
        while True:
            for state in self.states:
                value = 0
                for action in list(self.action_probabilities.keys()):
                    next_state, reward = self.next_state_and_reward(state, action)
                    if reward > 30:
                        value += self.special_case_probability[action] * (reward + self.gamma * self.state_values[next_state])
                    else:
                        value += self.action_probability[action] * (reward + self.gamma * self.state_values[next_state])
                new_state_values[state] = value
            
            if np.sum(np.abs(new_state_values - self.state_values)) < self.learning_tolerance:
                self.state_values = new_state_values.copy()
                break
        
    def move(self):
        
        self.grid[self.position] = ' '
        adjacent_values = {}
        for key in self.movements.keys():
            adjacent_values.update({tuple(sum(ele) for ele in zip(self.position, self.movements[key])) : 
                                    self.state_values[tuple(sum(ele) for ele in zip(self.position, self.movements[key]))]})
        #for state in adjacent_values:
            
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        