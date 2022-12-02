import numpy as np


def find_desired_angle(position_vector: list[float, float], speed: float, other_position: list[float, float], other_velocity: list[float, float]) -> float:
    """
    Finds angle ship should be at when trying to shoot a specific asteroid
    Returned angle is 0-360 going counter-clockwise with 0 in the positive y direction
    """
    a = other_velocity[1]*(position_vector[0]-other_position[0]) - other_velocity[0]*(position_vector[1]-other_position[1])
    b = (position_vector[0]-other_position[0])*speed
    c = (position_vector[1]-other_position[1])*speed
    theta = 2*np.arctan(np.sqrt(-a**2+b**2+c**2-c)/(a+b))
    desired_angle = theta*180/np.pi
    if desired_angle > 0:
        return desired_angle
    else:
        return desired_angle + 360

if __name__ == "__main__":
    position_vector = [0,0]
    speed = 4*np.sqrt(2)
    other_position = [4,0]
    other_velocity = [0,4]
    angle = find_desired_angle(position_vector, speed, other_position, other_velocity)
    print(angle)