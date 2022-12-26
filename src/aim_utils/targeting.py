import numpy as np
from src.vector_utils.trajectories import *

def target_first(
    position_vector: list[float, float],
    speed: float,
    other_position: list[float, float],
    other_velocity: list[float, float],
    ships_info
):
    firing_angle = find_desired_angle(position_vector, speed, other_position, other_velocity)


    abs_distance = ((position_vector[0]-other_position[0])**2 + (position_vector[1]-other_position[1])**2)**0.5

    if abs(firing_angle - ships_info[0]['angle']) + (abs_distance/3000) > 0.5:
        return False
    else:
        return True

def target_closest(input_data):

    frame = input_data['frame']
    time = input_data['time']
    stopping_condition = input_data['stopping_condition']
    asteroids = input_data['asteroids']
    map_dimensions = input_data['map_dimensions']
    bullets = input_data['bullets']
    ships_info = input_data['ships']
    print(ships_info)
    # print('test')
    # BROKEN CURRENTLY 
    # ship_position = ships_info(0)['position']

    # # AIMING

    ship_x = ships_info[0]['position'][0]
    ship_y = ships_info[0]['position'][1]
    ship_position = [ship_x, ship_y]

    speed = 800
    abs_distance = 1000000

    while ships_info[0]['angle'] < 0:
        ships_info[0]['angle'] = ships_info[0]['angle'] + 360

    print("---------------")
    print(asteroids)
    for x in asteroids:
        asteroid_x = x['position'][0]
        asteroid_y = x['position'][1]
        asteroid_position = [asteroid_x, asteroid_y]

        asteroid_x_speed = x['velocity'][0]
        asteroid_y_speed = x['velocity'][1]
        asteroid_velocity = [asteroid_x_speed, asteroid_y_speed]

        # firing_angle = find_desired_angle(ship_position, speed, asteroid_position, asteroid_velocity)

        abs_distance_temp = ((asteroid_x-ship_x)**2 + (asteroid_y + ship_y)**2)**0.5
        if abs_distance_temp < abs_distance:
            abs_distance = abs_distance_temp
            closest_asteroid = x

        # Optimize these distance and angle things by hand or ga
        # This method of checking the current angle and comparing is NOT GOOD! Leads to shots being lead or not lead enough because the ship is rotating before it reaches the angle. 
        # Included a quick distance measure so the angle we have is smaller at larger distances
        # Think the angle to make a shot in pool at 5 ft vs 20 ft

    asteroid_x = closest_asteroid['position'][0]
    asteroid_y = closest_asteroid['position'][1]
    asteroid_position = [asteroid_x, asteroid_y]

    asteroid_x_speed = closest_asteroid['velocity'][0]
    asteroid_y_speed = closest_asteroid['velocity'][1]
    asteroid_velocity = [asteroid_x_speed, asteroid_y_speed]


    firing_angle = find_desired_angle(ship_position, speed, asteroid_position, asteroid_velocity)
    abs_distance = ((asteroid_x-ship_x)**2 + (asteroid_y + ship_y)**2)**0.5

    if abs(firing_angle - ships_info[0]['angle']) + (abs_distance/3000) < 1:
        return 0
    elif 180 > (firing_angle + 360) - ships_info[0]['angle'] > 0 or 180 > firing_angle - ships_info[0]['angle'] > 0:
        return 1
    else:
        return -1
