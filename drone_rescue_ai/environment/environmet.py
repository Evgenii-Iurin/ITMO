import gymnasium as gym
from gymnasium import spaces
import numpy as np
import unittest


# Define the environment class
class SimpleDotGameEnv(gym.Env):
    def __init__(self):
        super(SimpleDotGameEnv, self).__init__()
        
        # Define action and observation space
        # Actions: 0 = up, 1 = down, 2 = left, 3 = right
        self.action_space = spaces.Discrete(4)
        
        # Observation space: player position (x, y)
        self.observation_space = spaces.Box(low=0, high=8, shape=(2,), dtype=np.int32)
        
        # Initial positions
        self.player_position = np.array([1, 1])
        self.flag_position = np.array([8, 8])
        self.obstacles = [
            np.array([3, 3]),
            np.array([5, 5]),
            np.array([7, 2])
        ]
        
        self.done = False

    def reset(self):
        # Reset the state of the environment to the initial position
        self.player_position = np.array([1, 1])
        self.done = False
        return self.player_position

    def step(self, action):
        # Define movement
        if action == 0:  # up
            new_position = self.player_position + np.array([0, -1])
        elif action == 1:  # down
            new_position = self.player_position + np.array([0, 1])
        elif action == 2:  # left
            new_position = self.player_position + np.array([-1, 0])
        elif action == 3:  # right
            new_position = self.player_position + np.array([1, 0])
        else:
            raise ValueError("Invalid action")

        # Check boundaries
        new_position = np.clip(new_position, 0, 8)

        # Check for collisions with obstacles
        if any((new_position == obstacle).all() for obstacle in self.obstacles):
            self.done = True
            reward = -1  # Negative reward for hitting an obstacle
            return self.player_position, reward, self.done, {}

        # Update player position
        self.player_position = new_position

        # Check if player reached the flag
        if (self.player_position == self.flag_position).all():
            self.done = True
            reward = 10  # Positive reward for reaching the flag
        else:
            reward = -0.1  # Small negative reward for each step to encourage shorter paths

        return self.player_position, reward, self.done, {}

    def render(self, mode='human'):
        # Print the environment in text form (for simplicity)
        grid = [['.' for _ in range(9)] for _ in range(9)]
        grid[self.flag_position[1]][self.flag_position[0]] = 'F'
        for obstacle in self.obstacles:
            grid[obstacle[1]][obstacle[0]] = 'X'
        grid[self.player_position[1]][self.player_position[0]] = 'P'
        
        print("\n".join(" ".join(row) for row in grid))
        print()

    def close(self):
        pass

# Example usage
# if __name__ == "__main__":
#     env = SimpleDotGameEnv()
#     obs = env.reset()
#     env.render()
    
#     done = False
#     while not done:
#         action = env.action_space.sample()  # Random action
#         obs, reward, done, info = env.step(action)
#         env.render()
#         print(f"Action: {action}, Reward: {reward}")

# Unit test for the environment
class TestSimpleDotGameEnv(unittest.TestCase):
    def setUp(self):
        self.env = SimpleDotGameEnv()

    # def test_initial_state(self):
    #     obs = self.env.reset()
    #     self.assertTrue((obs == np.array([1, 1])).all())
    #     self.assertFalse(self.env.done)

    # def test_step_up(self):
    #     self.env.reset()
    #     obs, reward, done, _ = self.env.step(0)  # Move up
    #     expected_position = np.array([1, 0])
    #     self.assertTrue((obs == expected_position).all())
    #     self.assertAlmostEqual(reward, -0.1)
    #     self.assertFalse(done)

    # def test_step_to_obstacle(self):
    #     self.env.reset()
    #     self.env.player_position = np.array([3, 2])  # Set position near an obstacle
    #     obs, reward, done, _ = self.env.step(1)  # Move down to hit obstacle
    #     self.assertTrue(done)
    #     self.assertAlmostEqual(reward, -1)

    # def test_reach_flag(self):
    #     self.env.reset()
    #     self.env.player_position = np.array([8, 7])  # Set position near the flag
    #     obs, reward, done, _ = self.env.step(1)  # Move down to reach the flag
    #     self.assertTrue(done)
    #     self.assertAlmostEqual(reward, 10)

    def test_go_out_from_the_range(self):
        self.env.reset()
        self.env.player_position = np.array([1, 1])
        _, reward, done, _ = self.env.step(0)
        print(self.env.player_position)
        self.env.render()

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
