from agent import Agent

import numpy as np
import matplotlib.pyplot as plt

import random

class NstepSarsaAgent(Agent):
    def __init__(self, environment, n, epsilon, discount_factor, step_size=1.0):
        super().__init__(environment)
        self.title = f"On policy n-step Sarsa agent (decaying ε-greedy)"

        self.qtable = np.full((environment.maze_height, environment.maze_width, len(environment.actions)), -1.)

        self.n = n
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
        self.time_step = -1 
        self.done = False
        self.current_iteration_path = []

        self.states = {0: self.environment.start_state} 
        self.rewards = {} 
        self.actions = {0: self.run_policy(self.environment.start_state)} 
        self.termination_time = np.inf
        self.epsilon *= 0.99

    def iteration_step(self):
        self.time_step += 1

        if self.time_step < self.termination_time:
            new_state, reward, self.done = self.environment.step(self.actions[self.time_step], self.states[self.time_step])
            self.states[self.time_step+1] = new_state
            self.rewards[self.time_step+1] = reward
            if self.done:
                self.termination_time = self.time_step + 1
            else:
                self.actions[self.time_step+1] = self.run_policy(self.states[self.time_step+1])

        # if enough states have been observed based on the value of self.n, then start
        # updating the q values for the 'time_step - self.n' actions
        time_to_update = self.time_step - self.n + 1
        if time_to_update >= 0:
            sy, sx = self.states[time_to_update]
            target = 0
            # sum all 'n' observed rewards
            for t in range(time_to_update+1, min(time_to_update+self.n, self.termination_time) + 1):
                target += (self.discount_factor**(t - time_to_update - 1)) * self.rewards[t]

            # add the bootstrapped current estimate for the rest of the time steps
            if time_to_update + self.n < self.termination_time:
                final_state_y, final_state_x = self.states[time_to_update+self.n]
                target += (self.discount_factor**self.n) * self.qtable[final_state_y, final_state_x, self.actions[time_to_update+self.n]]

            self.qtable[sy, sx, self.actions[time_to_update]] += self.step_size * (target - self.qtable[sy, sx, self.actions[time_to_update]])

        self.state = new_state

        self.current_iteration_path.append((*self.state, (200, 200, 0)))

        if self.done:
            self.termination_time = self.time_step + 1
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
