# Follow Centerline + Speed

def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    speed_factor = 0.2

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.6 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.8
    elif distance_from_center <= marker_3:
        reward = 0.7
    else:
        reward = 1e-3 # likely crashed/ close to off track
        return float(reward)

    # Add higher reward for higher speeds
    reward += speed * speed_factor



    return float(reward)

#-------------------------------------------------------------------------------------------------

# Follow the centerline + speed + all wheels on track

def track_check(params):
    # Check if all wheels are on track and add reward
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


#-------------------------------------------------------------------------------------------------

# Speed Only with Penalty for Offtrack

def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']

    # Calculate markers that are at varying distances away from the center line
    marker_3 = 0.6 * track_width

    # If car goes far from center, penalize the reward
    if distance_from_center >= marker_3:
        reward = -100
        return float(reward)

    # If car within bounds, reward = current speed
    reward = speed

    return float(reward)


#-------------------------------------------------------------------------------------------------

# Reward function emphasizing speed, staying on a smooth path, staying on track, and following the centerline

class Reward:

    def __init__(self, verbose=False, track_time=False):
        self.prev_speed = 0

    def speed_reward_fun(self, params):
        # Add a reward if the speed is faster than the previous speed
        speed = params['speed']
        reward = 0
        if (speed > self.prev_speed) and (self.prev_speed > 0):
            reward += 10
        self.prev_speed = speed  # update the previous speed
        return reward  # return the calculated reward

    def path_reward_fun(self, params):
        # Add penalty based on difference between current heading and heading of third future waypoint
        waypoints = params['waypoints']
        third_point = params['closest_waypoint'][1] + 2

        if third_point > len(waypoints):
            third_point -= len(waypoints)

        # Determine x and y coords of third waypoint
        y_3 = waypoints[third_point][1]
        x_3 = waypoints[third_point][0]

        reward = 0

        # Calculate angle difference

        angle_diff = math.atan2(y_3 - params['y'], x_3 - params['x'])

        reward -= angle_diff * 5

        return reward

    def center_reward_fun(self,params):

        track_width = params['track_width']
        distance_from_center = params['distance_from_center']

        # Calculate 3 markers that are at varying distances away from the center line
        marker_1 = 0.1 * track_width
        marker_2 = 0.25 * track_width
        marker_3 = 0.6 * track_width

        # Give higher reward if the car is closer to center line and vice versa
        if distance_from_center <= marker_1:
            reward = 10
        elif distance_from_center <= marker_2:
            reward = 8
        elif distance_from_center <= marker_3:
            reward = 5
        else:
            reward = 1e-3 # likely crashed/ close to off track
        return reward


reward_obj = Reward()

def reward_function(params):
  
    # Combine the three parts into one reward
    speed_reward = reward_obj.speed_reward_fun(params)

    path_reward = reward_obj.path_reward_fun(params)

    center_reward = reward_obj.path_reward_fun(params)

    final_reward = speed_reward + path_reward + center_reward

    # Return penalty if it goes off track
    if params['is_offtrack']:
        final_reward = -100

    return float(final_reward)
