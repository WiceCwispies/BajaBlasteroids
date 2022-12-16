import numpy as np


def find_desired_angle(
    position_vector: list[float, float],
    speed: float,
    other_position: list[float, float],
    other_velocity: list[float, float],
) -> float:
    """
    Finds angle ship should be at when trying to shoot a specific asteroid
    Returned angle is 0-360 going counter-clockwise with 0 in the positive y direction
    """
    a = -other_velocity[1]
    b = position_vector[0] - other_position[0]
    c = speed
    d = -other_velocity[0]
    f = position_vector[1] - other_position[1]
    theta = 2 * np.arctan((b*c - np.sqrt(-(a**2 * b**2) + 2*a*b*d*f + b**2 * c**2 + f**2*(c**2 - d**2)))/(a*b - f*(c+d)))
    
    desired_angle = 90 + (theta * 180 / np.pi)
    if desired_angle < 0:
        return desired_angle + 360
    else:
        return desired_angle


if __name__ == "__main__":
    position_vector = [300, 500]
    speed = 50*2**(0.5)
    other_position = [300,550]
    other_velocity = [50,0]
    angle = find_desired_angle(position_vector, speed, other_position, other_velocity)
    print(angle)
