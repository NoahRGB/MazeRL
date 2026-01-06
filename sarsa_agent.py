from agent import Agent

import numpy as np
import matplotlib.pyplot as plt

import random

class SarsaAgent(Agent):
    def __init__(self, environment, epsilon, discount_factor, step_size=1.0):
        super().__init__(environment)
        self.title = f"On policy TD(0) (sarsa, ε-greedy)"

        self.qtable = np.full((environment.maze_height, environment.maze_width, len(environment.actions)), -1.)

        self.epsilon = epsilon
        self.discount_factor = discount_factor
        self.step_size = step_size

        self.completed_iterations = 0
        self.trajectory_length_history = []
        self.reset_iteration()

    def run_policy(self, state):
        legal_moves = self.environment.get_legal(state)
        if random.random() < self.epsilon:
            return random.choice(legal_moves)
        else:
            # Greedy policy
            y, x = state 
            q_values = self.qtable[y, x, :] # Fetch from the q-table the 4 q-values for this current state (The 4 q-values correspond to actions North, South, West, East)
            legal_q_values = self.qtable[y, x, legal_moves]
            best_q_value = legal_q_values.max() # identify the best q_value
            best_q_indices = np.argwhere(q_values == best_q_value).flatten().tolist() # find all those occurences of the max q-value
            best_q_indices = [index for index in best_q_indices if index in legal_moves]
            return np.random.choice(best_q_indices) # if multiple q values have the maximum value, then choose one of them randomly

    def reset_iteration(self):
        # configuation for the current iteration
        self.state = self.environment.start_state
        self.time_step = 0
        self.done = False
        self.current_iteration_path = []

        self.current_action = self.run_policy(self.state)
        self.epsilon *= 0.99

    def iteration_step(self):
        self.time_step += 1
        new_state, reward, self.done = self.environment.step(self.current_action, self.state)

        next_action = self.run_policy(new_state)

        current_state_y, current_state_x = self.state
        next_state_y, next_state_x = new_state
        next_q_value = self.qtable[next_state_y, next_state_x, next_action]
        self.qtable[current_state_y, current_state_x, self.current_action] += self.step_size * (reward + self.discount_factor * next_q_value - self.qtable[current_state_y, current_state_x, self.current_action])

        self.state = new_state
        self.current_action = next_action

        self.current_iteration_path.append((*self.state, (200, 200, 0)))

        if self.done:
            self.trajectory_length_history.append(self.time_step)
            self.completed_iterations += 1

    def learn(self, iterations, quiet=False):
        for episode in range(iterations):
            self.reset_iteration()
            while not self.done:
                self.iteration_step()
            if not quiet: print(f"iteration {episode}, length: {self.trajectory_length_history[-1]}")

    def plot(self):
        plt.plot(self.trajectory_length_history)
        plt.ylabel("Trajectory Length")
        plt.yscale("log")
        plt.xlabel("Iteration")
        plt.grid()
        plt.show()

    def __str__(self):
        return f"ε = {round(self.epsilon, 2)}, γ = {self.discount_factor}, α = {self.step_size}"
