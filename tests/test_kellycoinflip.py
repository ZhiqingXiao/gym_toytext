import gym
import gym_toytext


def test_keyllycoinflip():
    env = gym.make('KellyCoinflip-v0')
    observation = env.reset()
    while True:
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            break
    env.close()


def test_keyllycoinflip_generalized():
    env = gym.make('KellyCoinflipGeneralized-v0')
    observation = env.reset()
    while True:
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            break
    env.close()
