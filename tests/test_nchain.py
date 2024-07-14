import gym
import gym_toytext


def test_nchain():
    env = gym.make("NChain-v0")
    observation, info = env.reset()
    while True:
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            break
    env.close()
