import pygame

def display_agents(agents, screen, font):
    xoff, yoff = 10, 10
    for agent in agents:
        env = agent.environment
        if agent != agents[0]:
            xoff += env.pixel_width + 10

        screen.blit(font.render(f"{agent.title}", False, (255, 0, 0)), (xoff, yoff + env.pixel_height))
        screen.blit(font.render(f"{agent}", False, (255, 0, 0)), (xoff, yoff + env.pixel_height + 25))
        screen.blit(font.render(f"episode: {agent.completed_iterations}", False, (0, 255, 0)), (xoff, yoff + env.pixel_height + 50))

        for state in agent.current_iteration_path:
            state_y, state_x, col = state
            pygame.draw.rect(screen, col, pygame.Rect(xoff + state_x * env.cell_size, yoff + state_y * env.cell_size, env.cell_size-0.5, env.cell_size-1))

        start_state_y, start_state_x = env.start_state
        goal_state_y, goal_state_x = env.goal_state
        current_state_y, current_state_x = agent.state
        pygame.draw.rect(screen, (0, 225, 0), pygame.Rect(xoff + start_state_x * env.cell_size, yoff + start_state_y * env.cell_size, env.cell_size, env.cell_size))
        pygame.draw.rect(screen, (0, 225, 0), pygame.Rect(xoff + goal_state_x * env.cell_size, yoff + goal_state_y * env.cell_size, env.cell_size, env.cell_size))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xoff + current_state_x * env.cell_size, yoff + current_state_y * env.cell_size, env.cell_size, env.cell_size))

        for i in range(0, len(env.maze)):
            for j in range(0, len(env.maze[i])):
                x_pos = xoff + j * env.cell_size
                y_pos = yoff + i * env.cell_size
                pygame.draw.rect(screen, (235, 235, 235), pygame.Rect(x_pos, y_pos, env.cell_size, env.cell_size), width=1)
                if env.maze[i][j] != 0:
                    pygame.draw.rect(screen, (235, 235, 235), pygame.Rect(x_pos, y_pos, env.cell_size, env.cell_size))
