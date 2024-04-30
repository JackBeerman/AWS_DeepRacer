# AWS DeepRacer
Machine Learning IV (Reinforcement Learning) Final Project

**Jack Beerman, Thomas Hammons, Conor McLaughlin, and Luke Rohlwing**

## Project Abstract
AWS DeepRacer provides students and developers an opportunity to incorporate Reinforcement Learning algorithms into a virtual or real robotics environment. It provides developers a platform through which they can construct a racecar agent's state space environment, define its goals, and specify its reward signal. In this paper, we explore the different racing behaviors exhibited by the DeepRacer RL agent racecar by comparing the agent's performance when it trains via the Proximal Policy Optimization (PPO) and Soft Actor-Critic (SAC) algorithms. After demonstrating that the PPO training algorithm outperforms the SAC learning process, we show the effects of various approaches to reward shaping. Despite certain resource constraints, such as a limited number of training hours through the free "student account" DeepRacer version, we provide evidence that a DeepRacer agent can be sufficiently trained to compete meaningfully in the monthly race challenges hosted by Amazon.

## Reward Functions and Methods
This repository includes all versions of the reward functions we tested for our Group Project. The initial iterations can be found [here](https://github.com/JackBeerman/AWS_DeepRacer/tree/main/Reward_Functions/Initial_Testing_Iterations). The reward function used in the PPO vs. SAC comparison can be found either [here](https://github.com/JackBeerman/AWS_DeepRacer/tree/main/Reward_Functions/PPO_Baseline) or [here](https://github.com/JackBeerman/AWS_DeepRacer/tree/main/Reward_Functions/SAC_Baseline). Finally, the final reward function and various versions of it (varying the weights for each part) can be found [here](https://github.com/JackBeerman/AWS_DeepRacer/tree/main/Reward_Functions/PPO_2.5) or in each of the files that begin with "Version".

The videos of the corresponding models can be found [here](https://drive.google.com/drive/folders/1SNJ8kO5DMKOlxdn2YVzVJt9qfAvDoUiP?usp=sharing).

## Results
Our best model completed the April 2024 compeititon ranked 53 out of 194 in the United States. This model corresponds to the reward function found under "Version_L" in this repository. A table of results can be seen below:

| Version         | Path Reward Weight | Lap Reward Weight | Fastest Lap Time | Overall Race Time | Reset Count |
|-----------------|--------------------|-------------------|------------------|-------------------|-------------|
|Baseline         | 1                  | 1                 | 58.5 s           | 3:12              | 7           |
|J                | 8                  | 9                 | 55.2 s           | 3:29              | 11          |
|L                | 3                  | 1                 | 45.1 s           | 2:27              | 2           |
|C                | 1                  | 5                 | 47.1 s           | 2:43              | 4           |
|T                | 6                  | 1                 | 48.6 s           | 2:27              | 0           |



