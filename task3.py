import matplotlib.pyplot as plt
import numpy as np
from task1 import projectile

def main():
    X, Y, g, u= float(input("X: ")), float(input("Y: ")), float(input("g: ")), float(input("u: "))
    min_u = np.sqrt(g)*np.sqrt(Y+np.sqrt(X**2+Y**2))
    min_theta = np.arctan((Y+np.sqrt(X**2+Y**2))/X)
    a = g/(2*u**2)*X**2
    b = -X
    c = Y + (g*X**2)/(2*u**2)
    low_high_theta = sorted([np.arctan((-b+np.sqrt(b**2-4*a*c))/(2*a)), np.arctan((-b-np.sqrt(b**2-4*a*c))/(2*a))])

    x1, y1 = projectile(g, 0, low_high_theta[1], u)
    x2, y2 = projectile(g, 0, min_theta, min_u)
    x3, y3 = projectile(g, 0, low_high_theta[0], u)

    plt.plot(x1, y1, marker='o', linestyle='-', color="blue", label="high ball", markersize=5, markerfacecolor='blue')
    plt.plot(x3, y3, marker='o', linestyle='-', color="orange", label="low ball", markersize=5, markerfacecolor='orange')
    plt.plot(x2, y2, marker='o', linestyle='-', color="grey", label="min u", markersize=5, markerfacecolor='grey')
    plt.plot(X, Y,'o', color='yellow', label="target")
    plt.title("Projectile to hig X, Y")
    plt.xlabel("x /m")
    plt.ylabel("y above launch height /m")

    plt.xlim(0, None)
    plt.ylim(0, None)

    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()