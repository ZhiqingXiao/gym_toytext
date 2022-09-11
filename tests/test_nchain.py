import gym
import gym_toytext


def test_nchain():
    env = gym.make("NChain-v0")
    observation, info = env.reset()
    while True:
        action = env.action_space.sample()
        observation, reward, termination, truncation, info = env.step(action)
        if termination or truncation:
            break
    env.close()
