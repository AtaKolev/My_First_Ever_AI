# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:26:07 2021

@author: atana
"""

import numpy as np

def lab_gen():

    x_y_dict = {'x' : np.arange(0,11),
                'y' : np.arange(0, 11)}
    lab_map_disp = []

    for y in range(len(x_y_dict['y'])-1, -1, -1):
        temp = []
        for x in range(0, len(x_y_dict['x'])):
            if x == 0 and (y in np.arange(0, 10)):
                if x == 0 and y == 1:
                    temp.append('O') # Entry point of the agent
                else:
                    temp.append('|')
            elif x == 10 and (y in np.arange(0, 10)):
                temp.append('|')
            elif y == 0 and (x in np.arange(0, 11)):
                temp.append('-')
            elif y == 10 and (x in np.arange(0, 11)):
                temp.append('-')
            elif x == 2 and (y in np.arange(1, 9)):
                temp.append('|')
            elif (x in np.arange(3, 6)) and y == 8:
                temp.append('-')
            elif x == 5 and (y in np.arange(2, 9)):
                temp.append('|')
            elif x == 4 and y == 2:
                temp.append('L')
            elif x == 4 and (y in np.arange(3, 9)):
                temp.append('|')
            elif (x == 3 and y == 7) or (x == 9 and y == 9):
                temp.append('S')
            elif (x in np.arange(7, 10) and y == 8):
                temp.append('-')
            elif x == 7 and (y in np.arange(2, 8)):
                temp.append('|')
            elif x == 8 and y == 2:
                temp.append('⅃')
            elif x == 8 and (y in np.arange(3, 8)):
                temp.append('|')
            elif x == 9 and y == 7:
                temp.append('R')
            else:
                temp.append(' ')
        lab_map_disp.append(temp)

    return lab_map_disp