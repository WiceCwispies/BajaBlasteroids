import numpy as np
from src.vector_utils.trajectories import *

def target_aquired(
    position_vector: list[float, float],
    speed: float,
    other_position: list[float, float],
    other_velocity: list[float, float],
    ships_info
):
    firing_angle = find_desired_angle(position_vector, speed, other_position, other_velocity)


    abs_distance = ((position_vector[0]-other_position[0])**2 + (position_vector[1]-other_position[1])**2)**0.5

    if abs(firing_angle - ships_info[0]['angle']) + (abs_distance/3000) > 1:
        return False
    else:
        return True