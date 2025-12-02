from q_learner import QLearner
from environment import MazeEnvironment

env = MazeEnvironment()
learner = QLearner(env, 0.1, 0.1, 1.0)

learner.learn(1000)
learner.plot()

# - We could use a decaying epsilon greedy policy to make the trajectory length converge to the optimal length.

# - If you experiment with setting epsilon to zero then it sometimes still works really well.
# This is very unusual.  It must be because the default Q-values of zero are higher than the final Q-values (which are all negative) 
# therefore exploration is encouraged towards rarely-visited locations.  But have a think about this.

# - A GUI showing the agent in the maze would be nice, but animations will slow down learning.