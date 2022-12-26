import numpy as np


def generate_heatmap(
    asteroid_positions: list[float, float],
    num_zones: list[float, float],
    game_size=[1000, 800],
):
    """
    Calculates the number of asteroids within the zones divided from the total game size.
    asteroid positions is simply a list of the x and y coordinates of each asteroid.
    num_zones is how many zones to break the game into in each direction.
    game_size is the total size of the game that will be broken up.
    """
    intervals = np.divide([sum(x) for x in zip(game_size, [0.001, 0.001])], num_zones)
    heatmap = np.zeros(num_zones)
    asteroid_positions = (np.floor_divide(asteroid_positions, intervals)).astype(int)
    for asteroid_position in asteroid_positions:
        heatmap[asteroid_position[1], asteroid_position[0]] += 1
    return heatmap

def heatmap_decision():
    x = 0

if __name__ == "__main__":
    asteroids_positions = [[1, 1], [2, 1], [2, 1], [2, 2], [1, 2]]
    num_zones = [2, 2]
    game_size = [2, 2]
    print(generate_heatmap(asteroids_positions, num_zones, game_size))
