#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 20:27:47 2022

@author: nasko
"""

import Code_Agent
import Labyrinth_generator as lg
import numpy as np
import pandas as pd

entry_point = (1,1)
row_size = 11
column_size = 11
wall_index = [(1, 0), (2, 0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (10, 0),
              (2,2), (3,2), (4,2), (5,2), (6,2), (7,2), (8,2), (9,2)]
stick_placement = [(1, 9), (3, 3)]
reward_placement = [(3, 9)]
labyrinth = lg.lab_gen()


