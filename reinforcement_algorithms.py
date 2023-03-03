import numpy as np
import constants



def next_state_and_reward(state, action, states):
        
        next_state = tuple(sum(ele) for ele in zip(state, constants.movements[action]))
        if next_state not in states:
            next_state = state
        
        if next_state in self.R_states:
            return next_state, self.treat
        elif next_state in self.S_states:
            return next_state, self.stick
        else:
            return next_state
        
def evaluate_state_values(states, state_values = None, position = None):
    
    if not state_values:
        state_values = {}
    for state in states:
        if state == position:
            continue
        state_values.update({state : 0})
    new_state_values = state_values.copy()
    
    while True:
        for state in states:
            value = 0
            for action in list(constants.action_probability.keys()):
                next_state, reward = next_state_and_reward(state, action)
                if next_state not in states:
                    continue
                if reward > 30:
                    value += constants.special_case_probability[action] * (reward + constants.gamma * state_values[next_state])
                else:
                    value += constants.action_probability[action] * (reward + constants.gamma * state_values[next_state])
            new_state_values[state] = value
        
        if np.sum(np.abs(np.array(list(new_state_values.values())) -\
                            np.array(list(state_values.values())))) < constants.learning_tolerance:
            #self.state_values = new_state_values.copy()
            for state in state_values.keys():
                state_values[state] = new_state_values[state]
            break