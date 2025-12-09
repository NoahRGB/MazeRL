from q_learner import QLearner, QLearnerStepper
from environment import MazeEnvironment
from maze_display import MazeDisplayer

import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 500))

max_iterations = 100

env = MazeEnvironment()
learner = QLearnerStepper(env, 0.1, 0.1, 1.0)
maze = env.get_env()
displayer = MazeDisplayer(10, 10, screen, env.get_env(), tuple(env.start_state), tuple(env.goal_state))

running = True
current_iteration = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if current_iteration < max_iterations:
        new_state, done = learner.iteration_step()
        displayer.update_path(tuple(new_state))
        displayer.display(current_iteration)

        if done:
            learner.initialise_iteration()
            current_iteration += 1
            if current_iteration < max_iterations:
                displayer.clear_path()
    else:
        displayer.display(current_iteration)
       
    pygame.display.flip()

pygame.quit()







# learner.plot()

# - We could use a decaying epsilon greedy policy to make the trajectory length converge to the optimal length.

# - If you experiment with setting epsilon to zero then it sometimes still works really well.
# This is very unusual.  It must be because the default Q-values of zero are higher than the final Q-values (which are all negative) 
# therefore exploration is encouraged towards rarely-visited locations.  But have a think about this.

# - A GUI showing the agent in the maze would be nice, but animations will slow down learning.
