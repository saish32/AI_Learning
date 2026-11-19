import gymnasium as gym
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random

class DQN(nn.Module):
    def __init__(self, state_size, action_size):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(state_size, 24)
        self.fc2 = nn.Linear(24, 24)
        self.fc3 = nn.Linear(24, action_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

#hyperparameters 
enviorment = 'CartPole-v1'
learning_rate=0.001
gamma=0.99
buffer_size=10000
batch_size=32
epsilon_start=1.0
target_update_frequency=10

#initialize environment and DQN
env=gym.make(enviorment)
input_size=env.observation_space.shape[0]
output_size=env.action_space.n
device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
policy_net=DQN(input_size, output_size).to(device)
target_net=DQN(input_size, output_size).to(device)
target_net.load_state_dict(policy_net.state_dict())
target_net.eval()

optimizer=optim.Adam(policy_net.parameters(), lr=learning_rate)
criterion=nn.MSELoss()

#experience replay buffer
replay_buffer=[]

def train(num_episodes):
    step_count=0 #initialize step count
    for episode in range(num_episodes):
        state, _ = env.reset() #reset environment and get initial state
        state=np.array(state, dtype=np.float32) #convert state to numpy array
        done=False
        total_reward=0
        while not done:
            #epsilon-greedy action selection
            if random.random() < epsilon_start:
                action=env.action_space.sample() #exploration
            else:
                with torch.no_grad():
                    state_tensor=torch.FloatTensor(state).unsqueeze(0).to(device)
                    action=policy_net(state_tensor).argmax().item() #exploitation

            #take action and observe next state and reward
            next_state, reward, done , truncated, _ = env.step(action)
            done=done or truncated #consider episode done if either done or truncated is True
            next_state=np.array(next_state, dtype=np.float32) #convert next state to numpy array
            total_reward+=reward #accumulate total reward

            #store transition in replay buffer
            replay_buffer.append((state, action, reward, next_state, done))
            if len(replay_buffer) > buffer_size:
                replay_buffer.pop(0) #remove oldest transition if buffer is full

            #update state
            state=next_state

            #sample a batch of transitions from the replay buffer and perform optimization
            if len(replay_buffer) >= batch_size:
                batch=random.sample(replay_buffer, batch_size)
                states, actions, rewards, next_states, dones=zip(*batch)

                #convert to tensors and move to device
                states=torch.FloatTensor(states).to(device)
                actions=torch.LongTensor(actions).unsqueeze(1).to(device)
                rewards=torch.FloatTensor(rewards).unsqueeze(1).to(device)
                next_states=torch.FloatTensor(next_states).to(device)
                dones=torch.FloatTensor(dones).unsqueeze(1).to(device)

                #compute Q-values and target Q-values
                q_values=policy_net(states).gather(1, actions)
                with torch.no_grad():
                    next_q_values=target_net(next_states).max(1)[0].unsqueeze(1)
                    target_q_values=rewards + (gamma * next_q_values * (1 - dones))

                #compute loss and perform optimization step
                loss=criterion(q_values, target_q_values.unsqueeze(1))
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                #update target network periodically
                step_count+=1
                if step_count % target_update_frequency == 0:
                    target_net.load_state_dict(policy_net.state_dict())
                print(f"Episode {episode+1}/{num_episodes}, Total Reward: {total_reward}, Loss: {loss.item():.4f}")

train(num_episodes=500)