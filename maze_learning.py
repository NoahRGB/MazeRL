from environment import MazeEnvironment
from on_policy_monte_carlo_agent import OnPolicyMonteCarloAgent
from off_policy_monte_carlo_agent import OffPolicyMonteCarloAgent
from sarsa_agent import SarsaAgent
from expected_sarsa_agent import ExpectedSarsaAgent
from nstep_sarsa_agent import NstepSarsaAgent
from qlearning_agent import QLearningAgent
from double_qlearning_agent import DoubleQLearningAgent
from maze_display import show_agents

import matplotlib.pyplot as plt


agents = [
        NstepSarsaAgent(MazeEnvironment(), n=4, epsilon=0.2, discount_factor=0.99),
        # DoubleQLearningAgent(MazeEnvironment(), epsilon=0.9, discount_factor=0.99),
        # QLearningAgent(MazeEnvironment(), epsilon=0.9, discount_factor=0.99),
        # SarsaAgent(MazeEnvironment(), epsilon=0.8, discount_factor=0.99),
        # ExpectedSarsaAgent(MazeEnvironment(), epsilon=0.9, discount_factor=0.99),
        # OnPolicyMonteCarloAgent(MazeEnvironment(), epsilon=0.9, discount_factor=0.99, every_visit=False),
        # OnPolicyMonteCarloAgent(MazeEnvironment(), epsilon=0.8, discount_factor=0.99, every_visit=False),
        # OnPolicyMonteCarloAgent(MazeEnvironment(), epsilon=0.7, discount_factor=0.99, every_visit=False),
        # OnPolicyMonteCarloAgent(MazeEnvironment(), epsilon=0.6, discount_factor=0.99, every_visit=False),
        # OnPolicyMonteCarloAgent(MazeEnvironment(), epsilon=0.5, discount_factor=0.99, every_visit=False),
        # OnPolicyMonteCarloAgent(MazeEnvironment(), epsilon=0.4, discount_factor=0.99, every_visit=False),
        # OnPolicyMonteCarloAgent(MazeEnvironment(), epsilon=0.3, discount_factor=0.99, every_visit=False),
        # OnPolicyMonteCarloAgent(MazeEnvironment(), epsilon=0.2, discount_factor=0.99, every_visit=False),
        # OnPolicyMonteCarloAgent(MazeEnvironment(), epsilon=0.1, discount_factor=0.99, every_visit=False),
        # OnPolicyMonteCarloAgent(MazeEnvironment(), epsilon=0.0, discount_factor=0.99, every_visit=False),
        # QLearnerAgent(MazeEnvironment(), epsilon=0.1, learning_rate=1.0, discount_factor=1.0),
        # QLearnerAgent(MazeEnvironment(), epsilon=0.0, learning_rate=1.0, discount_factor=1.0),
        # QLearnerAgent(MazeEnvironment(), epsilon=0.1, learning_rate=0.1, discount_factor=1.0),
]

# show_agents(agents)

agents[0].learn(1000, quiet=False)
agents[0].plot()







