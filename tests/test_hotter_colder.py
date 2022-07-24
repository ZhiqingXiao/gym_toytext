import gym
import gym_toytext


def test_hotter_colder():
    env = gym.make("HotterColder-v0")
    observation = env.reset()
    low, high = env.action_space.low, env.action_space.high
    while True:
        action = (low + high) / 2.
        observation, reward, done, info = env.step(action)
        if done:
            break
        if observation == 1:
            low = action
        elif observation == 3:
            high = action
    env.close()
