import numpy as np
import random

#define the environment(4x4 grid)
num_states = 16 #4x4 grid has 16 states
num_actions = 4 # 0=up, 1=down, 2=left, 3=right
q_tables=np.zeros((num_states, num_actions)) #initialize Q-table with zeros

#define the parameters
alpha = 0.1 #learning rate
gamma = 0.9 #discount factor
epsilon = 0.2 #exploration rate
nums_episodes = 1000 #number of episodes

#define a simple reward structure for the grid
reward_structure = np.zeros(num_states)
reward_structure[15] = 1 #goal state with reward of 1

#function to determine the next state based on the current state and action
def get_next_state(state, action):
    if action == 0 and state >= 4: #up
        return state - 4 
    elif action == 1 and state < 12: #down
        return state + 4 
    elif action == 2 and state % 4 != 0: #left
        return state - 1 
    elif action == 3 and state % 4 != 3: #right
        return state + 1 
    else:
        return state #if action is invalid, stay in the same state

#q-learning algorithm
for episode in range(nums_episodes):
    state=random.randint(0, num_states - 1) #start from a random state
    while state != 15: #continue until reaching the goal state
        if random.uniform(0, 1) < epsilon: #exploration
            action=random.randint(0, num_actions - 1)
        else: #exploitation
            action=np.argmax(q_tables[state]) #choose the action with the highest Q-value

        next_state=get_next_state(state, action) #get the next state based on the current state and action
        reward=reward_structure[next_state] #get the reward for the next state
        old_q_value=q_tables[state, action] #get the old Q-value for the current state and action
        next_max_q_value=np.max(q_tables[next_state]) #get the maximum Q-value for the next state

        #update Q-table using the Q-learning formula
        new_q_value=old_q_value + alpha * (reward + gamma * next_max_q_value - old_q_value)
        q_tables[state, action]=new_q_value #update the Q-table with the new Q

        state=next_state #move to the next state

#display the learned Q-table
print("Learned Q-table:")
print(q_tables)
