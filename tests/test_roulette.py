import gym
import gym_toytext


def test_roulette():
    env = gym.make("Roulette-v0")
    observation = env.reset()
    while True:
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            break
    env.close()
