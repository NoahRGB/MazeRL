import random
import numpy as np
import matplotlib.pyplot as plt

class QLearner:
  def __init__(self, environment, epsilon, learning_rate, discount_factor):
    self.environment = environment
    self.qtable = np.zeros((environment.maze_height, environment.maze_width, len(environment.actions)), dtype=np.float64)
    self.epsilon = epsilon
    self.learning_rate = learning_rate
    self.discount_factor = discount_factor

  def run_policy(self, current_state):
      # epsilon greedy
      if random.random() < self.epsilon:
          return random.choice([0, 1, 2, 3])
      else:
          # Greedy policy
          y, x = current_state
          q_values = self.qtable[y,x,:] # Fetch from the q-table the 4 q-values for this current state (The 4 q-values correspond to actions North, South, West, East)
          best_q_value = q_values.max() # identify the best q_value
          best_q_indices = np.argwhere(q_values == best_q_value).flatten().tolist() # find all those occurences of the max q-value
          return np.random.choice(best_q_indices) # if multiple q values have the maximum value, then choose one of them randomly

  def apply_q_update(self, state, action, reward, next_state, done, discount_factor):
      sy, sx = state
      nsy, nsx = next_state
      current_q_value = self.qtable[sy, sx, action]
      all_q_values_at_next_state = self.qtable[nsy, nsx, :]

      if done:
          target_q_value = reward
      else:
          target_q_value = reward + discount_factor * np.max(all_q_values_at_next_state)
      self.qtable[sy, sx, action] += self.learning_rate * (target_q_value - current_q_value) #update
      return current_q_value, state
  
  def learn(self, iterations, quiet=False):
    self.reward_history = []
    self.trajectory_length_history = []
    for iteration in range(iterations):
        state = self.environment.start_state
        total_reward = 0
        done = False
        time_step = 0
        while not done:
            # Choose an action
            action = self.run_policy(state)
            #print("time_step",time_step,"state",state,"action",action)
            next_state, reward, done = self.environment.step(action, state)
            #print("action",action, "next_state", next_state, "reward",reward, "done", done)
            
            self.apply_q_update(state, action, reward, next_state,  done, self.discount_factor)

            state = next_state
            total_reward += reward * (self.discount_factor**time_step)
            time_step += 1
            if time_step > 50000:
                raise Exception("Should have solved it by now - something is wrong with the code")
            
        self.reward_history.append(total_reward)
        self.trajectory_length_history.append(time_step)
        
        if not quiet:
          print("Iteration", iteration, "Done.  Total_reward=", total_reward, "Trajectory length", time_step)
          print(f"Last reward: {self.reward_history[-1]}, last trajectory length: {self.trajectory_length_history[-1]}")

  def plot(self):
    plt.plot(self.trajectory_length_history)
    plt.ylabel('Trajectory Length')
    plt.yscale('log')
    plt.xlabel('Iteration')
    plt.grid()
    plt.show()
