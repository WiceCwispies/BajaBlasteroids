import numpy as np
from src.vector_utils.trajectories import *

def angle_to_speed(
    angle_desired,
    current_angle
) -> float:

    a = angle_desired
    c = current_angle

    if 180 > (a + 360) - c > 0 or 180 > a - c > 0:
        s = a - c
    else:
        s = c - a

    return s