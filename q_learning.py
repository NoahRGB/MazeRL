from environment import MazeEnvironment
from q_learner_agent import QLearnerAgent
from on_policy_monte_carlo_agent import OnPolicyMonteCarloAgent
from off_policy_monte_carlo_agent import OffPolicyMonteCarloAgent
from maze_display import display_agents 

import pygame
import matplotlib.pyplot as plt

import time

WIDTH, HEIGHT = 1500, 600
max_iterations = 50 
running = True
interactive = False 

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 25)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

agents = [
        OnPolicyMonteCarloAgent(MazeEnvironment(), epsilon=0.4, discount_factor=1.0, every_visit=True),
        QLearnerAgent(MazeEnvironment(), epsilon=0.1, learning_rate=1.0, discount_factor=1.0),
        # QLearnerAgent(MazeEnvironment(), epsilon=0.0, learning_rate=1.0, discount_factor=1.0),
        # QLearnerAgent(MazeEnvironment(), epsilon=0.1, learning_rate=0.1, discount_factor=1.0),
]

while running:
    screen.fill((40, 40, 40))
    for event in pygame.event.get():
        running = not event.type == pygame.QUIT

    if (interactive and pygame.key.get_pressed()[pygame.K_SPACE]) or not interactive: 
        for agent in agents:
            if agent.completed_iterations < max_iterations:
                agent.iteration_step()
                if agent.done and agent.completed_iterations < max_iterations:
                    agent.reset_iteration()
            elif not agent.finished_episodes:
                agent.final_episode()

    display_agents(agents, screen, font)

    pygame.display.flip()


# agents[0].learn(1000, quiet=True)
# agents[0].plot()

pygame.quit()









