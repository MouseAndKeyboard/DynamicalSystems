
from matplotlib import pyplot as plt

# x_t = a*x_{t-1} + b, x_0 = 1
class System:
    def __init__(self, starting_x=0, a=1.1, b=1.1, dt=0.1):
        self.a = a
        self.b = b
        self.x = starting_x
        self.t = 0
        self.dt = dt
        self.result = [self.x]
        self.timesteps = [self.t]

    def observe(self):
        self.result.append(self.x)
        self.timesteps.append(self.t)

    def update(self):
        self.x = self.a * self.x + self.b
        self.t += self.dt

    def run(self, time):
        while(self.t < time):
            self.update()
            self.observe()

    def plot(self):
        plt.plot(self.timesteps, self.result)
        plt.show()

s = System(a=1.01, b=10, dt=0.01)
s.run(10)
s.plot()
