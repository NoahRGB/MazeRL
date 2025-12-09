from q_learner import QLearner, QLearnerStepper
from environment import MazeEnvironment
from maze_display import MazeDisplayer

import pygame

import time

WIDTH, HEIGHT = 2000, 1200
# MAZE_WIDTH, MAZE_HEIGHT = 250, 530
MAZE_WIDTH, MAZE_HEIGHT = 1000, 530


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
max_iterations = 500
env = MazeEnvironment()

learners = []
current_yoff = 10
current_xoff = 10
configs = [
    {"epsilon" : 0.01, "learning_rate" : 1.0, "discount_factor" : 1.0},
    {"epsilon" : 0.01, "learning_rate" : 1.0, "discount_factor" : 1.0},
]
# configs = [
#     {"epsilon" : 0.1, "learning_rate" : 0.1, "discount_factor" : 1.0},
#     {"epsilon" : 0.1, "learning_rate" : 0.5, "discount_factor" : 1.0},
#     {"epsilon" : 0.1, "learning_rate" : 1.0, "discount_factor" : 1.0},
#     {"epsilon" : 0.1, "learning_rate" : 1.0, "discount_factor" : 1.0},
#     {"epsilon" : 0.1, "learning_rate" : 1.0, "discount_factor" : 1.0},
#     {"epsilon" : 0.1, "learning_rate" : 1.0, "discount_factor" : 1.0},
#     {"epsilon" : 0.1, "learning_rate" : 1.0, "discount_factor" : 1.0},
#     {"epsilon" : 0.1, "learning_rate" : 1.0, "discount_factor" : 1.0},
#     {"epsilon" : 0.1, "learning_rate" : 1.0, "discount_factor" : 1.0},
#     {"epsilon" : 0.1, "learning_rate" : 1.0, "discount_factor" : 1.0}
# ]
for i in range(0, len(configs)):
    if current_xoff >= WIDTH - MAZE_WIDTH:
        current_xoff = 10
        current_yoff += MAZE_HEIGHT
    learners.append({
        "learner": QLearnerStepper(MazeEnvironment(), epsilon=configs[i]["epsilon"], learning_rate=configs[i]["learning_rate"], discount_factor=configs[i]["discount_factor"]),
        "displayer": MazeDisplayer(current_xoff, current_yoff, screen, MazeEnvironment()),
        "current_iteration": 1
    })
    current_xoff += MAZE_WIDTH

running = True
for learner in learners: learner["start_time"] = time.perf_counter()
while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for learner in learners:
        font = pygame.font.SysFont("Comic Sans MS", 20)
        text = f"ε = {learner['learner'].epsilon}, η = {learner['learner'].learning_rate}, γ = {learner['learner'].discount_factor}"
        text_surface = font.render(text, False, (0, 255, 0))
        xpos, ypos = learner['displayer'].xoff, learner['displayer'].yoff + len(learner['displayer'].maze) * learner['displayer'].cell_size + 30
        screen.blit(text_surface, (xpos, ypos))
        
        if learner["current_iteration"] < max_iterations:
            new_state, done = learner["learner"].iteration_step()
            learner["displayer"].update_path(tuple(new_state))
            learner["displayer"].display(learner["current_iteration"])

            if done:
                learner["learner"].initialise_iteration()
                learner["current_iteration"] += 1
                if learner["current_iteration"] < max_iterations:
                    learner["displayer"].clear_path()
        else:
            if not "time_taken" in learner: learner["time_taken"] = time.perf_counter() - learner["start_time"]
            learner["displayer"].display(learner["current_iteration"])
            text_surface = font.render(f"Finished in {round(learner["time_taken"], 2)} seconds", False, (255, 0, 0))
            screen.blit(text_surface, (xpos, ypos + 30))

       
    pygame.display.flip()

pygame.quit()
