import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
import gymnasium as gym

#setup the environment
env=gym.make('CartPole-v1')
state_shape=int(env.observation_space.shape[0])
num_actions=int(env.action_space.n)

#parameters
learning_rate=0.01
gamma=0.99
num_episodes=1000

#policy network
def build_policy_model():
    model=tf.keras.Sequential([
        layers.Input(shape=(state_shape,)),
        layers.Dense(24, activation='relu'),
        layers.Dense(24, activation='relu'),
        layers.Dense(num_actions, activation='softmax')
    ])
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate), loss='categorical_crossentropy') 
    return model

policy_model=build_policy_model()

#function to select action based on policy
def select_action(state):
    state=np.array(state).reshape(1, state_shape) #ensure state is in the right shape
    action_probs=policy_model.predict(state, verbose=0) #get action probabilities from the policy network
    action=np.random.choice(num_actions, p=action_probs[0]) #sample an action                                       
    return action, action_probs[0]

#function to calculate returns (discouned reards)
def discounted_rewards(rewards):
    discounted=np.zeros_like(rewards, dtype=np.float32)
    cumulative=0.0
    for i in reversed(range(len(rewards))):
        cumulative=rewards[i]+gamma*cumulative
        discounted[i]=cumulative
    return discounted-np.mean(discounted) #normalize the discounted rewards

#training function
def train_on_episodes(states, actions, rewards):
    discounted=discounted_rewards(rewards) #calculate discounted rewards
    with tf.GradientTape() as tape:
        action_probs=policy_model(tf.convert_to_tensor(states, dtype=tf.float32)) #get action probabilities for all states
        action_indices=tf.stack([tf.range(len(actions)), actions], axis=1) #get indices of the taken actions

        selected_action_probs=tf.gather_nd(action_probs, action_indices) #get probabilities of the taken actions
        loss=-tf.reduce_mean(tf.math.log(selected_action_probs)*discounted) #calculate the loss
    grads=tape.gradient(loss, policy_model.trainable_variables) #compute gradients
    policy_model.optimizer.apply_gradients(zip(grads, policy_model.trainable_variables)) #update the policy network

#main training loop
for episodes in range(num_episodes):
    state, _ = env.reset() #reset the environment and get the initial state
    done=False
    states=[]
    actions=[]
    rewards=[]
    while not done:
        action, _ = select_action(state) #select an action based on the current state
        next_state, reward, done, truncated, _ = env.step(action) #take the action and observe the next state and reward
        done=done or truncated #check if the episode is done

        states.append(state) #store the current state
        actions.append(action) #store the taken action
        rewards.append(reward) #store the received reward

        state=next_state #move to the next state

    if done:
        train_on_episodes(states, actions, rewards) #train the policy network on the collected episode data
        print(f"Episode {episodes+1}/{num_episodes} completed with total reward: {sum(rewards)}") #print the total reward for the episode
