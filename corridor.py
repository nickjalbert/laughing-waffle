import gym


class Corridor(gym.Env):
    metadata = {"render.modes": ["human"]}
    action_space = (0, 1)

    def __init__(self, config=None):
        config = config if config else {}
        self.length = config.get("length", 10)
        self.reset()

    def step(self, action):
        if self.done:
            return (self.position, 0, self.done, {})
        if action == 0 and self.position > 0:
            self.position -= 1
        if action == 1 and self.position < self.length:
            self.position += 1
        return (self.position, -1, self.done, {})

    @property
    def done(self):
        return self.position >= self.length

    def reset(self):
        self.position = 0
        return (self.position,)

    def render(self, mode="human"):
        pass

    def close(self):
        pass
