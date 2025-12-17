from environment import MazeEnvironment
from q_learner_agent import QLearnerAgent
from maze_display import display_agents 

import pygame
import matplotlib.pyplot as plt

import time

WIDTH, HEIGHT = 1500, 600
max_iterations = 50 
running = True

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 20)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

agents = [
        QLearnerAgent(MazeEnvironment(), epsilon=0.1, learning_rate=1.0, discount_factor=1.0),
        QLearnerAgent(MazeEnvironment(), epsilon=0.0, learning_rate=1.0, discount_factor=1.0),
        # QLearnerAgent(MazeEnvironment(), epsilon=0.1, learning_rate=0.1, discount_factor=1.0),
]

while running:
    screen.fill("black")
    for event in pygame.event.get():
        running = not event.type == pygame.QUIT
       
    for agent in agents:
        if agent.completed_iterations <= max_iterations:
            agent.iteration_step()
            if agent.done and agent.completed_iterations < max_iterations: agent.reset_iteration()

    display_agents(agents, screen, font)

    pygame.display.flip()


pygame.quit()









