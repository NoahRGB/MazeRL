import pygame
import numpy as np

class MazeDisplayer:
    def __init__(self, xoff, yoff, screen, maze, start_cell, goal_cell, cell_size=25, background_color="black"):
       self.xoff = xoff
       self.yoff = yoff
       self.screen = screen
       self.maze = maze
       self.start_cell = start_cell
       self.goal_cell = goal_cell
       self.background_colour = background_color
       self.cell_size = cell_size 
       self.font = pygame.font.SysFont("Comic Sans MS", 30)
       self.clear_path()
        
    def display(self, iteration_num):
        self.screen.fill(self.background_colour)
        text_surface = self.font.render(f"Iteration: {iteration_num}", False, (255, 0, 0)) 
        self.screen.blit(text_surface, (self.xoff, self.yoff + len(self.maze) * self.cell_size))
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[i])):
                x_pos = self.xoff + j * self.cell_size
                y_pos = self.yoff + i * self.cell_size
                if (i, j) == self.start_cell:
                    pygame.draw.rect(self.screen, "green", pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size))
                elif (i, j) == self.goal_cell:
                    pygame.draw.rect(self.screen, "green", pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size))
                elif (i, j) in self.current_path:
                    pygame.draw.rect(self.screen, "yellow", pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size))
                elif self.maze[i][j] == 0:
                    pygame.draw.rect(self.screen, "white", pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size), width=1)
                else:
                    pygame.draw.rect(self.screen, "white", pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size))
    
    def update_path(self, cell):
        self.current_path.append(cell)

    def clear_path(self):
        self.current_path = [self.start_cell]

if __name__ == "__main__":
    maze = np.array([
        [1,1,1,1,1,1,1,1,1],
        [1,0,1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1,0,1],
        [1,0,0,0,1,0,1,0,1],
        [1,1,1,0,1,0,1,0,1],
        [1,0,0,0,1,0,1,0,1],
        [1,0,1,1,1,0,1,1,1],
        [1,0,1,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,1,0,1],
        [1,0,1,1,1,0,1,0,1],
        [1,0,0,0,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1]])

    
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    running = True

    displayer = MazeDisplayer(10, 10, screen, maze, (1, 1))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        displayer.display()

        pygame.display.flip()

    pygame.quit()
