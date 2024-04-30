import math

class Reward:
    def __init__(self, verbose=False, track_time=False):
        self.prev_quarter_steps = 0
        pass

    def path_reward_fun(self, params):
        current_heading = params['heading']
        waypoints = params['waypoints']
        third_point = params['closest_waypoints'][1] + 2

        if third_point >= len(waypoints):
            third_point -= len(waypoints)

        y_3 = waypoints[third_point][1]
        x_3 = waypoints[third_point][0]

        reward = 0

        optim_heading = math.atan2(y_3 - params['y'], x_3 - params['x'])

        optim_heading = math.degrees(optim_heading)

        angle_diff = abs(optim_heading - current_heading)

        reward = (-angle_diff) / 180

        return reward

    def finishing_lap_reward_fun(self, params):

        waypoints = params['waypoints']
        len_waypoints = len(waypoints)
        next_waypoint_idx = params['closest_waypoints'][1]
        steps = params['steps']

        steps_this_quarter = steps - self.prev_quarter_steps

        reward = 0

        if int(next_waypoint_idx) == len_waypoints // 4:
            reward += 100
            penalty_per_step = steps_this_quarter * 0.5
            reward -= penalty_per_step
            self.prev_quarter_steps = steps

        elif int(next_waypoint_idx) == len_waypoints // 2:
            reward += 100
            penalty_per_step = steps_this_quarter * 0.5
            reward -= penalty_per_step
            self.prev_quarter_steps = steps

        elif int(next_waypoint_idx) == int(len_waypoints*0.75):
            reward += 100
            penalty_per_step = steps_this_quarter * 0.5
            reward -= penalty_per_step
            self.prev_quarter_steps = steps

        elif int(next_waypoint_idx) == len_waypoints:
            reward += 100
            penalty_per_step = steps_this_quarter * 0.5
            reward -= penalty_per_step
            self.prev_quarter_steps = steps

        reward = max(0, reward)

        return reward

reward_obj = Reward()

def reward_function(params):

    path_reward = reward_obj.path_reward_fun(params)

    lap_reward = reward_obj.finishing_lap_reward_fun(params)

    path_reward_weight = 8 #try different values
    lap_reward_weight = 9 #try different values

    final_reward = path_reward_weight * path_reward + lap_reward * lap_reward_weight

    if params['is_offtrack']:
        final_reward = -1000

    return float(final_reward)