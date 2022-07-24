import gym
import gym_toytext


def test_nchain():
    env = gym.make("NChain-v0")
    observation = env.reset()
    while True:
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            break
    env.close()
