#!/usr/bin/env python3.9

from matplotlib import pyplot as plt

class System:
    def __init__(self, starting_x=1, a=1.1, dt=0.1):
        self.a = a
        self.x = starting_x
        self.t = 0
        self.dt = dt
        self.result = [self.x]
        self.timesteps = [self.t]

    def observe(self):
        self.result.append(self.x)
        self.timesteps.append(self.t)

    def update(self):
        self.x = self.x * self.a
        self.t += self.dt

    def run(self, time):
        while(self.t < time):
            self.update()
            self.observe()

    def plot(self):
        plt.plot(self.timesteps, self.result)
        plt.show()

s = System(a=1.01)
s.run(10)
s.plot()
