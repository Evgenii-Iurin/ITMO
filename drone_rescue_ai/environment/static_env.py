import numpy as np
from PIL import Image, ImageColor


class Environment():
    def __init__(self):
        self.area_size = 100 # one side side
        self.num_targets = 10 # number of targets
        self.num_obstacles = 50 # number of obstacles   
        self.obstacles_map = {
            0: (4, 2),
            1: (3, 5),
            2: (5, 5),
            3: (2, 10),
            4: (10, 2),
        }
        self.color_map = {
            0: 'white', # background
            1: 'black', # obstacle
            2: 'red', # target point
            10: 'gray'
        }
        self.area = np.zeros((self.area_size, self.area_size))
        self.observation_area = (9,9) # drone observation area TODO: should be as agent parameter
        self.visited_area = np.full((self.area_size, self.area_size), 10)
        self._generate_area()

    def _generate_area(self):
        # TODO : set attribute if None
        obstacles_x, obstacles_y = self.get_random_x_y(self.area_size, self.num_obstacles)        
        target_point_x, target_point_y = self.get_random_x_y(self.area_size, 1)
        
        # Add obstacles
        for x, y in zip(obstacles_x, obstacles_y):
            sampled_obstacle = self.obstacles_map[
                np.random.choice(list(self.obstacles_map.keys()))
                ]
            self._insert_kernel(sampled_obstacle, (x, y), 1)
        
        # Add target point
        self._insert_kernel((3, 3), (target_point_x, target_point_y), 2)

    def _insert_kernel(self, kernel_shape: tuple[int, int], point: tuple[int, int], fill_with: int):
        start_row, end_row, start_col, end_col = self._calculate_edges_of_kernel(self.area, kernel_shape, point)
        self.area[start_row:end_row, start_col:end_col] = fill_with


    def get_observation(self, agent_position: tuple[int, int]) -> np.ndarray:
        start_row, end_row, start_col, end_col = self._calculate_edges_of_kernel(self.area, self.observation_area, agent_position)
        observation = self.area[start_row:end_row, start_col:end_col] 
        self._update_visited_area(start_row, end_row, start_col, end_col, observation)
        return observation

    def _update_visited_area(self, start_row, end_row, start_col, end_col, observation):
        self.visited_area[start_row:end_row, start_col:end_col] = observation

    @staticmethod
    def get_random_x_y(max_size: int, num_of_samples: int) -> list[int] | int:
        x = np.random.randint(0, max_size, num_of_samples)
        y = np.random.randint(0, max_size, num_of_samples)
        if num_of_samples == 1:
            x, y = x[0], y[0]
        return x, y
    
    @staticmethod
    def _calculate_edges_of_kernel(area: np.ndarray, kernel_shape: tuple[int, int], point: tuple[int, int]):
        kernel_center = (kernel_shape[0] // 2, kernel_shape[1] // 2)
        start_row = max(point[0] - kernel_center[0], 0)
        end_row = min(point[0] + kernel_center[0] + 1, area.shape[0])
        start_col = max(point[1] - kernel_center[1], 0)
        end_col = min(point[1] + kernel_center[1] + 1, area.shape[1])
        return start_row, end_row, start_col, end_col
    
    def save_env_as_image(self, save_path):
        """
        Saves a 2D numpy array as a JPEG image using a specified color map.

        Parameters:
        - env_array: 2D numpy array where each cell represents a specific color based on `color_map`.
        - color_map: Dictionary mapping integer values to colors (e.g., {0: 'white', 1: 'red'}).
        - save_path: Path where the JPEG image will be saved.

        """
        height, width = self.area.shape
        img = Image.new("RGB", (width, height))
        for y in range(height):
            for x in range(width):
                value = self.area[y, x]
                color = self.color_map.get(value, 'black')  # Use 'black' as a fallback if value not in color_map
                img.putpixel((x, y), ImageColor.getrgb(color))

        img.save(save_path, format="JPEG")

    def save_observation(self, observation: np.ndarray, save_path: str):
        height, width = observation.shape
        img = Image.new("RGB", (width, height))
        for y in range(height):
            for x in range(width):
                value = observation[y, x]
                color = self.color_map.get(value, 'black')  # Use 'black' as a fallback if value not in color_map
                img.putpixel((x, y), ImageColor.getrgb(color))

        img.save(save_path, format="JPEG")

    def save_visited_area(self, save_path: str):
        height, width = self.visited_area.shape
        img = Image.new("RGB", (width, height))
        for y in range(height):
            for x in range(width):
                value = self.visited_area[y, x]
                color = self.color_map.get(value, 'black')  # Use 'black' as a fallback if value not in color_map
                img.putpixel((x, y), ImageColor.getrgb(color))

        img.save(save_path, format="JPEG")

# !HOW TO USE!
# if __name__ == "__main__":
#     env = Environment()
#     print(env.area)
#     env.save_env_as_image('./env.jpg')
#     observation = env.get_observation((20, 30))
#     observation = env.get_observation((25, 30))
#     observation = env.get_observation((30, 30))
#     observation = env.get_observation((35, 30))
#     observation = env.get_observation((40, 30))
#     observation = env.get_observation((45, 30))
#     env.save_observation(observation, './observation.jpg')
#     env.save_visited_area('./visited_area.jpg')
