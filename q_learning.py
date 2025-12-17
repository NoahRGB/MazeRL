from q_learner import QLearner, QLearnerStepper
from environment import MazeEnvironment
from agent import QLearnerAgent
from maze_display import MazeDisplayer, MazeDisplayerNew

import pygame
import matplotlib.pyplot as plt

import time

WIDTH, HEIGHT = 1500, 700
# MAZE_WIDTH, MAZE_HEIGHT = 250, 530
MAZE_WIDTH, MAZE_HEIGHT = 1000, 530

def dislay_agents(agents, screen, cell_size=25):
    xoff, yoff = 10, 10
    for agent in agents:
        env = agent.environment
        for i in range(0, len(env.maze)):
            for j in range(0, len(env.maze[i])):
                x_pos = xoff + j * cell_size
                y_pos = yoff + i * cell_size
                if (i, j) == env.start_state:
                    pygame.draw.rect(screen, "green", pygame.Rect(x_pos, y_pos, cell_size, cell_size))
                elif (i, j) == env.goal_state:
                    pygame.draw.rect(screen, "green", pygame.Rect(x_pos, y_pos, cell_size, cell_size))
                elif (i, j) in agent.current_iteration_path:
                    pygame.draw.rect(screen, "yellow", pygame.Rect(x_pos, y_pos, cell_size, cell_size))
                elif env.maze[i][j] == 0:
                    pygame.draw.rect(screen, "white", pygame.Rect(x_pos, y_pos, cell_size, cell_size), width=1)
                else:
                    pygame.draw.rect(screen, "white", pygame.Rect(x_pos, y_pos, cell_size, cell_size))

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
max_iterations = 500

agent = QLearnerAgent(MazeEnvironment(), 0.1, 1.0, 1.0)
agent.reset_iteration()
while agent.completed_iterations < max_iterations:
    agent.iteration_step()
    dislay_agents([agent], screen)
    # print(agent.trajectory_length_history[-1])
    if agent.done:
        agent.reset_iteration()
    pygame.display.flip()





# plt.plot(agent.trajectory_length_history)
# plt.ylabel("Trajectory Length")
# plt.yscale("log")
# plt.xlabel("Iteration")
# plt.grid()
# plt.show()

pygame.quit()
