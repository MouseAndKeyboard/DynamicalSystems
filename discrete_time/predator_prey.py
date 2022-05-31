#!/usr/bin/env python3.9
from matplotlib import pyplot as plt

class System:
    def __init__(self, starting_x=1, starting_y=1, r=0.5, d=0.5, b=0.5, c=0.5, K=1.1, dt=0.1):
        self.r = r
        self.d = d
        self.b = b
        self.c = c
        self.K = K
        self.x = starting_x
        self.y = starting_y
        self.t = 0
        self.dt = dt
        self.result = [[self.x], [self.y]]
        self.timesteps = [self.t]

    def observe(self):
        self.result[0].append(self.x)
        self.result[1].append(self.y)
        self.timesteps.append(self.t)

    def update(self):
        denom = (self.b * self.y + 1)
        print(denom)
        if (denom == 0):
            print('uh oh')
            denom = 0   .1

        new_x = self.x + self.r * self.x *(1 - (self.x / self.K)) - (1 - 1/denom) * self.x
        new_y = self.y - self.d * self.y - self.c * self.x * self.y
        self.x = new_x
        self.y = new_y
        self.t += self.dt

    def run(self, time):
        while(self.t < time):
            self.update()
            self.observe()

    def plot(self):
        fig, ax = plt.subplots()
        ax.plot(self.timesteps, self.result[0])
        ax.plot(self.timesteps, self.result[1])
        plt.show()

s = System(starting_x=1, starting_y=1, r=1, b=1, d=1, c=1, K=5, dt=0.01)
s.run(1)
s.plot()
