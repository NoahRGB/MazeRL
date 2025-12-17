import pygame

def display_agents(agents, screen, font):
    xoff, yoff = 10, 10
    for agent in agents:
        env = agent.environment
        if agent != agents[0]:
            xoff += env.pixel_width + 10
        screen.blit(font.render(f"{agent.title}", False, (255, 0, 0)), (xoff, yoff + env.pixel_height))
        screen.blit(font.render(f"{agent}", False, (255, 0, 0)), (xoff, yoff + env.pixel_height + 25))
        screen.blit(font.render(f"iteration: {agent.completed_iterations}", False, (0, 255, 0)), (xoff, yoff + env.pixel_height + 50))
        for i in range(0, len(env.maze)):
            for j in range(0, len(env.maze[i])):
                x_pos = xoff + j * env.cell_size
                y_pos = yoff + i * env.cell_size
                if [i, j] == env.start_state:
                    pygame.draw.rect(screen, "green", pygame.Rect(x_pos, y_pos, env.cell_size, env.cell_size))
                elif [i, j] == env.goal_state:
                    pygame.draw.rect(screen, "green", pygame.Rect(x_pos, y_pos, env.cell_size, env.cell_size))
                elif [i, j] == agent.state:
                    pygame.draw.rect(screen, "red", pygame.Rect(x_pos, y_pos, env.cell_size, env.cell_size))
                elif [i, j] in agent.current_iteration_path:
                    pygame.draw.rect(screen, "yellow", pygame.Rect(x_pos, y_pos, env.cell_size, env.cell_size))
                elif env.maze[i][j] == 0:
                    pygame.draw.rect(screen, "white", pygame.Rect(x_pos, y_pos, env.cell_size, env.cell_size), width=1)
                else:
                    pygame.draw.rect(screen, "white", pygame.Rect(x_pos, y_pos, env.cell_size, env.cell_size))
