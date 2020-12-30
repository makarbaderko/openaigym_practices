import gym
env = gym.make('MountainCarContinuous-v0')

observation = env.reset()

#print(env.action_space)

for i in range(1000):
   env.render()
   if i < 20:
       observation, reward, done, info = env.step([-1.0])
   else:
      observation, reward, done, info = env.step([1.0])
   if done:
      break