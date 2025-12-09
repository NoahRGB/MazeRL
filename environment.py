import numpy as np


class MazeEnvironment:
  def __init__(self):
    self.maze = np.array([
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

    self.maze_width = self.maze.shape[1]
    self.maze_height = self.maze.shape[0]
    self.start_state = [1,1]
    self.goal_state = [self.maze_height-2, self.maze_width-2]
    self.actions = ["North", "South", "West", "East"]
    self.action_effects = [ [-1, 0 ], [ 1, 0 ], [ 0, -1 ], [ 0, 1 ] ]
  
  def step(self, action, state):
      assert type(action) in [int, np.int64, np.int32]
      assert action < len(self.action_effects) and action >= 0
      y, x = state
      dy, dx = self.action_effects[action]
      new_x = x + dx
      new_y = y + dy
      if new_x < 0 or new_x >= self.maze_width:
          # off grid
          new_x = x
      if new_y < 0 or new_y >= self.maze_height:
          # off grid
          new_y = y
      if self.maze[new_y, new_x] == 1:
          # hit wall
          new_y = y
          new_x = x
      new_state = [new_y, new_x]
      reward = -1
      done = (new_state==self.goal_state)
      return new_state, reward, done

  def get_env(self):
      return self.maze
