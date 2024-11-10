import numpy as np
from PIL import Image, ImageColor


class Environment():
    def __init__(self):
        self.area_size = 100 # one side side
        self.num_targets = 10 # number of targets
        self.num_obstacles = 30 # number of obstacles   
        self.obstacles = [
            np.array([1, 1, 1]),
            np.array([[1], [1], [1]])
        ]
        self._generate_area()
        self.color_map = {
            0: 'white', 
            1: 'red'
        }

    def _generate_area(self):
        # TODO : set attribute if None
        self.area = np.zeros((self.area_size, self.area_size))
        obstacles_x = np.random.randint(0, self.area_size, self.num_obstacles)
        obstacles_y = np.random.randint(0, self.area_size, self.num_obstacles)
        for x, y in zip(obstacles_x, obstacles_y):
            self.area[x, y] = 1
        
        self.area[0,0] = 1

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


if __name__ == "__main__":
    env = Environment()
    print(env.area)
    env.save_env_as_image('./env.jpg')
