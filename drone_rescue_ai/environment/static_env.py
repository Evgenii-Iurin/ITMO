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
            2: 'red' # target point
        }
        self._generate_area()

    def _generate_area(self):
        # TODO : set attribute if None
        self.area = np.zeros((self.area_size, self.area_size))
        obstacles_x = np.random.randint(0, self.area_size, self.num_obstacles)
        obstacles_y = np.random.randint(0, self.area_size, self.num_obstacles)
        
        target_point_x = np.random.randint(0, self.area_size)
        target_point_y = np.random.randint(0, self.area_size)
        
        # Add obstacles
        for x, y in zip(obstacles_x, obstacles_y):
            sampled_obstacle = self.obstacles_map[
                np.random.choice(list(self.obstacles_map.keys()))
                ]
            self._insert_kernel(sampled_obstacle, (x, y), 1)
        
        # Add target point
        self._insert_kernel((3, 3), (target_point_x, target_point_y), 2)

    def _insert_kernel(self, kernel_shape: tuple[int, int], point: tuple[int, int], fill_with: int):
        kernel_center = (kernel_shape[0] // 2, kernel_shape[1] // 2)
        start_row = max(point[0] - kernel_center[0], 0)
        end_row = min(point[0] + kernel_center[0] + 1, self.area.shape[0])
        start_col = max(point[1] - kernel_center[1], 0)
        end_col = min(point[1] + kernel_center[1] + 1, self.area.shape[1])
        self.area[start_row:end_row, start_col:end_col] = fill_with


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


# !HOW TO USE!
# if __name__ == "__main__":
#     env = Environment()
#     print(env.area)
#     env.save_env_as_image('./env.jpg')
