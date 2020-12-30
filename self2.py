import gym
import time
from IPython.display import clear_output
import numpy as np

"""
синий цвет указывает на пассажира;
пурпурный - пункт назначения;
желтый - наше пустое такси;
зеленый - такси при полном;
буквы R, G, Y, B - места.
0: двигаться на юг;
1: двигаться на север;
2: двигаться на восток;
3: двигаться на запад;
4: пикап пассажира;
5: высадка пассажира.
"""

max_iter = 1000
done = False
history = []

env = gym.make("Taxi-v3").env
env.reset()
env.render()

class Q:
    def __init__(self):
        self.gamma=0.95
        self.alpha=0.05
        self.state={}
        self.q_table = np.zeros((state_size, action_size))

    def get_state(self):
        return history[-1]
    def save_state(self, state):
        history.append(state)
print("Started")
for i in range(max_iter):
    #Get next step
    if done:
        print(f"Finished after {i} iterations")
print("Finished")


env.render()