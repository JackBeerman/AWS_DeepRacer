def track_check(params):
    
    wheel_check = params["all_wheels_on_track"]
    reward = 0
    
    if wheel_check:
        reward = 1.0
    else:
        reward = 0.0
    
    return reward
    
def speed_distance(params):
    reward = 0
    
    progress = params["progress"]
    speed = params["speed"]
    
    
    if progress > 0.5:
        if speed > 3:
            reward = 2
    else:
        reward = 0
    
    return reward


def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    
    ## run new function of track check
    add_on = track_check(params)
    
    ## check speed
    speed = speed_distance(params)

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
        reward += add_on
        reward += speed
    elif distance_from_center <= marker_2:
        reward = 0.5
        reward += add_on
        reward += speed
    elif distance_from_center <= marker_3:
        reward = 0.1
        reward += speed
    else:
        reward = 1e-2 # likely crashed/ close to off track

    return float(reward)
