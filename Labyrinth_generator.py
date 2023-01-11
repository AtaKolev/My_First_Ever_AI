# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:26:07 2021

@author: atana
"""

import numpy as np

def lab_gen(entry_point: tuple, X: int, Y: int,
            wall_indexes: list, L_indexes: list, reverse_L_indexes: list,
            dash_indexes: list,
            stick_placement: list, reward_placement: list,
            reward_letter: str, stick_letter: str):
    
    for lst in [wall_indexes, L_indexes, reverse_L_indexes, dash_indexes,
                stick_placement, reward_placement]:
        for ele in lst:
            if (ele[0] > X) or (ele[1] > Y):
                raise ValueError(f"Element: {ele} in {lst} beyond limits!")
    
    lab_map_disp = []
    for y in range(0, Y):
        temp = []
        for x in range(0, X):
            # if x == 0 and (y in np.arange(0, column_size)):
            #     if (x, y) == entry_point:
            #         temp.append('O')
            #     else:
            #         temp.append('|')
            # elif x == row_size-1 and (y in np.arange(0, column_size-1)):
            #     temp.append('|')
            # elif y == 0 and (x in np.arange(0, row_size - 1)):
            #     temp.append('-')
            # elif y == column_size and (x in np.arange(0, row_size-1)):
            #     temp.append('-')
            # elif (x in x_wall) and (y in np.arange(1, 9)):
            #     temp.append('|')
            # elif (x in np.arange(3, 6)) and y == 8:
            #     temp.append('-')
            # elif x == 5 and (y in np.arange(2, 9)):
            #     temp.append('|')
            # elif x == 4 and y == 2:
            #     temp.append('L')
            # elif x == 4 and (y in np.arange(3, 9)):
            #     temp.append('|')
            # elif (x, y) in stick_placement:
            #     temp.append('S')
            # elif (x in np.arange(7, 10) and y == 8):
            #     temp.append('-')
            # elif x == 7 and (y in np.arange(2, 8)):
            #     temp.append('|')
            # elif x == 8 and y == 2:
            #     temp.append('⅃')
            # elif x == 8 and (y in np.arange(3, 8)):
            #     temp.append('|')
            # elif (x, y) in reward_placement:
            #     temp.append('R')
            # else:
            #     temp.append(' ')
            if (x,y) in wall_indexes:
                temp.append(' ')
            elif (x, y) in stick_placement:
                temp.append('S')
            elif (x, y) in reward_placement:
                temp.append('R')
            elif (x, y) in L_indexes:
                temp.append(' ')
            elif (x, y) in reverse_L_indexes:
                temp.append(' ')
            elif (x, y) in dash_indexes:
                temp.append('-')
            elif (x, y) == entry_point:
                temp.append('O')
            else:
                temp.append(' ')
        lab_map_disp.append(temp)

    return lab_map_disp