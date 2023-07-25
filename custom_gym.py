import gymnasium as gym
from gymnasium import spaces
from random import randint
import numpy as np
import keyboard
import time

####
##GYM


class env(gym.Env):
    def __init__(self, action_space, observation_space):
        self.action_space = spaces.Discrete(action_space)
        self.observation_space = spaces.Box(low = -observation_space,high = observation_space)
        self.max = observation_space #variable for render

    def reset(self,seed=None):
        self.observation = np.array([randint(-self.max, self.max)], dtype=np.float32)
        return self.observation, {}

    def step(self, action):
        position = self.observation
        # if action == 0:
        #     position += 0
        if action == 1:
            if position != -self.max:
                position -= 1
        if action == 2:
            if position != self.max:
                position += 1

        reward = np.float64(-np.abs(position))
        self.observation = np.array(position)
        terminated = False
        truncated = False   
        return self.observation,reward,terminated,truncated,{}

    def render(self):
        player_position = 0 + self.observation
        video = ""  # variable that stores board
        for x in range(-self.max, self.max + 1):
            if x == player_position:
                video += "$"  # add player
            else:
                video += "^"
        print(video)

    # for manual control
    def manual_control(self):
        pos = self.reset()
        self.render()
        while True:
            if keyboard.is_pressed("left"):
                pos = self.step(0)
                self.render()
                time.sleep(0.1)
            if keyboard.is_pressed("right"):
                pos = self.step(1)
                self.render()
                time.sleep(0.1)

    def close(self):
        pass
    