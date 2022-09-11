import gym
import gym_toytext


def test_roulette():
    env = gym.make("Roulette-v0")
    observation, info = env.reset()
    while True:
        action = env.action_space.sample()
        observation, reward, termination, truncation, info = env.step(action)
        if termination or truncation:
            break
    env.close()
