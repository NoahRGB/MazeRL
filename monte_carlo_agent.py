from agent import Agent

import numpy as np

class MonteCarloAgent(Agent):
    def __init__(self, environment, epsilon):
        super().__init__(environment)
        self.qtable = np.zeros((environment.maze_height, environment.maze_width, len(environment.actions)), dtype=np.float64)
        self.epsiilon = epsilon

    def run_policy(self, state):
        pass

    def learn(self, iterations, quiet=False):

        for i in range(iterations):
            state = self.environment.start_state
            done = False
            rewards = []

            while not done:
                action = self.run_policy(self.state)
                next_state, reward, done = self.environment.step(action, self.state)



    def __str__(self):
        return ""

