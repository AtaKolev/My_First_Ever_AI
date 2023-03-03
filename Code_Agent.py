import numpy as np
import time
import constants

class Agent:
    
    def __init__(self,  gamma, learning_tolerance):
        
        self.actions = list(constants.action_probability.keys())
        print(self.grid)
        
        
    def move(self):
        
        finished_move = False
        adjacent_values = {}
        for key in self.movements.keys():
            if tuple(sum(ele) for ele in zip(self.position, self.movements[key])) not in list(self.state_values.keys())+self.S_states+self.R_states:
                continue
            if tuple(sum(ele) for ele in zip(self.position, self.movements[key])) in self.passed_states:
                continue
            if tuple(sum(ele) for ele in zip(self.position, self.movements[key])) in self.S_states+self.R_states:
                self.position = tuple(sum(ele) for ele in zip(self.position, self.movements[key]))
                finished_move = True
                break
            adjacent_values.update({tuple(sum(ele) for ele in zip(self.position, self.movements[key])) : 
                                    self.state_values[tuple(sum(ele) for ele in zip(self.position, self.movements[key]))]})
        
        if not finished_move:
            self.passed_states.append(self.position) 
            self.position = max(adjacent_values, key = adjacent_values.get)
    
    def visualize_move(self):
        
        self.grid[self.position] = ' '
        self.move()
        self.grid[self.position] = 'O'
        print(self.grid)
        time.sleep(1)
                    
    def finish(self):

        finished = False

        if (self.grid[self.position] in self.reward_letter) or (self.grid[self.position] in self.stick_letter):
            print("Run Finished!")
            print("Restart by running the loop again")
            print(self.grid)
            finished = True

        return finished