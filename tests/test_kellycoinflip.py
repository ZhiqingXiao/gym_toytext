import gym
import gym_toytext


def test_keyllycoinflip():
    env = gym.make('KellyCoinflip-v0')
    observation, info = env.reset()
    while True:
        action = env.action_space.sample()
        observation, reward, termination, truncation, info = env.step(action)
        if termination or truncation:
            break
    env.close()


def test_keyllycoinflip_generalized():
    env = gym.make('KellyCoinflipGeneralized-v0')
    observation, info = env.reset()
    while True:
        action = env.action_space.sample()
        observation, reward, termination, truncation, info = env.step(action)
        if termination or truncation:
            break
    env.close()
