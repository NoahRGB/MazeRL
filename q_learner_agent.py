from agent import Agent
from environment import Environment

import numpy as np
import matplotlib.pyplot as plt

import random

class QLearnerAgent(Agent):
    def __init__(self, environment: Environment, epsilon, learning_rate, discount_factor):
        super().__init__(environment)
        self.title = "Tabular Q Learning"
        self.finished_episodes = False
        self.qtable = np.zeros((environment.maze_height, environment.maze_width, len(environment.actions)), dtype=np.float64)
        self.epsilon = epsilon
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.completed_iterations = 0

        self.reward_history = []
        self.trajectory_length_history = []
        self.reset_iteration()

    def final_episode(self):
        self.reset_iteration()
        saved_epsilon = self.epsilon
        self.epsilon = 0
        self.learn(1, quiet=True)
        self.epsilon = saved_epsilon 
        self.finished_episodes = True

    def run_policy(self, state):
        # epsilon greedy
        if random.random() < self.epsilon:
            return random.choice([0, 1, 2, 3])
        else:
            # Greedy policy
            y, x = state 
            q_values = self.qtable[y, x, :] # Fetch from the q-table the 4 q-values for this current state (The 4 q-values correspond to actions North, South, West, East)
            best_q_value = q_values.max() # identify the best q_value
            best_q_indices = np.argwhere(q_values == best_q_value).flatten().tolist() # find all those occurences of the max q-value
            return np.random.choice(best_q_indices) # if multiple q values have the maximum value, then choose one of them randomly

    def apply_q_update(self, state, action, reward, next_state, done, discount_factor):
        sy, sx = state
        nsy, nsx = next_state
        current_q_value = self.qtable[sy, sx, action]
        all_q_values_at_next_state = self.qtable[nsy, nsx, :]

        if done:
            target_q_value = reward
        else:
            target_q_value = reward + discount_factor * np.max(all_q_values_at_next_state)
        self.qtable[sy, sx, action] += self.learning_rate * (target_q_value - current_q_value) #update
        return current_q_value, state

    def iteration_step(self):
        # Choose an action
        action = self.run_policy(self.state)
        next_state, reward, self.done = self.environment.step(action, self.state)

        self.apply_q_update(self.state, action, reward, next_state, self.done, self.discount_factor)

        self.state = next_state
        self.current_iteration_path.append((*self.state, (200, 200, 0)))
        self.total_reward += reward * (self.discount_factor**self.time_step)
        self.time_step += 1

        if self.done:
            self.completed_iterations += 1
            self.trajectory_length_history.append(self.time_step)
            self.reward_history.append(self.total_reward)

    def reset_iteration(self):
        # configuation for the current iteration
        self.state = self.environment.start_state
        self.total_reward = 0
        self.time_step = 0
        self.done = False
        self.current_iteration_path = []

    def learn(self, iterations, quiet=False):
        for iteration in range(iterations):
            self.reset_iteration()
            while not self.done:
                self.iteration_step()
                if self.time_step > 50000:
                    raise Exception("Learning is taking too long")

            if not quiet:
              print("Iteration", iteration, "Done.  Total_reward=", self.total_reward, "Trajectory length", self.time_step)
              print(f"Last reward: {self.reward_history[-1]}, last trajectory length: {self.trajectory_length_history[-1]}")

    def plot(self):
        plt.plot(self.trajectory_length_history)
        plt.ylabel("Trajectory Length")
        plt.yscale("log")
        plt.xlabel("Iteration")
        plt.grid()
        plt.show()

    def __str__(self):
        return f"ε = {self.epsilon}, η = {self.learning_rate}, γ = {self.discount_factor}"

