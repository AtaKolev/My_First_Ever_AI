 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 20:27:47 2022

@author: nasko
"""

from Code_Agent import Agent
import Labyrinth_generator as lg
import numpy as np



def main():
    entry_point = (0,9)
    x_count = 11
    y_count = 11
    wall_index = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
                (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9),
                (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9),
                (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7),
                (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
                (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7),
                (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)]
            
    stick_placement = [(9, 1), (3, 3)]
    reward_placement = [(9, 3)]
    L_index = [(4, 8), (7, 8)]
    reverse_L_indexes = [(5, 8), (8, 8)]
    dash_indexes = [(0,0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0),
                    (0,10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10),
                    (3, 2), (4, 2), (8, 2), (9, 2)]
    reward_letter = 'R'
    stick_letter = 'S'
    labyrinth = lg.lab_gen(entry_point, x_count, y_count, wall_index,
                        L_index, reverse_L_indexes, dash_indexes, stick_placement,
                        reward_placement, reward_letter, stick_letter)

    ca = Agent(starting_position = (9, 0),
                    grid = np.array(labyrinth),
                    gamma = 0.9, treat = 100, stick = -100, learning_tolerance = 1e-4,
                    reward_letter = reward_letter, stick_letter = stick_letter)

    while True:
        
        ca.evaluate_state_values()
        ca.visualize_move()
        if ca.finish():
            break
        else:
            continue
        

if __name__ == '__main__':
    main()


















