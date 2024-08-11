import matplotlib.pyplot as plt
import numpy as np
from task1 import projectile
def main():
    theta, g, u, h = float(input("Angle from horizontal: ")), float(input("Gravity: ")), float(input("Speed: ")), float(input("Height: "))
    theta_rad = np.radians(theta)
    analytic(g, h, theta_rad, u)
    plt.show()
def analytic(g, h, theta, u, intervals=0.05, limx=None, limy=None, color="black"):
    def func(x):
        return np.tan(theta)*x - g/(2*u**2)*(1+np.tan(theta)**2)*x**2 + h
    X, Y = [], []
    T = 0
    while True:
        x =  T*u*np.cos(theta)
        y = func(x)
        X.append(x)
        Y.append(y)
        if y < 0:
            break
        T += intervals
    x, y = projectile(g, h, theta, u)
    plt.plot(x, y, marker='o', linestyle='-', color=color, markersize=5, markerfacecolor="blue")
    plt.plot(x[list(y).index(max(y))], max(y), "*", label="apogee", markersize=12, color="orange")
    plt.title('Projectile trajectory')
    plt.xlabel('x /m')
    plt.ylabel('y above launch height /m')
    plt.ylim(0, limy)
    plt.xlim(0, limx)   
    plt.grid(True)
if __name__ == "__main__":
    main()



