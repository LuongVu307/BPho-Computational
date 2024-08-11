import matplotlib.pyplot as plt
import numpy as np
from task1 import projectile

def main():
    X, Y, g, u, h = float(input("X: ")), float(input("Y: ")), float(input("g: ")), float(input("u: ")), float(input("h: "))
    min_u = np.sqrt(g)*np.sqrt(Y+np.sqrt(X**2+Y**2))
    min_theta = np.arctan((Y+np.sqrt(X**2+Y**2))/X)

    a = g/(2*u**2)*X**2
    b = -X
    c = Y - h + (g*X**2)/(2*u**2)
    low_high_theta = sorted([np.arctan((-b+np.sqrt(b**2-4*a*c))/(2*a)), np.arctan((-b-np.sqrt(b**2-4*a*c))/(2*a))])
    theta_max = np.arcsin(1/np.sqrt(2+(2*g*h)/(u**2)))
    bounding = lambda x : u**2/(2*g) - g/(2*u**2)*x**2 + h
    x_bounding = np.linspace(0, u**2/g, 200)

    x1, y1 = projectile(g, h, low_high_theta[0], u)
    x2, y2 = projectile(g, 0, min_theta, min_u)
    x3, y3 = projectile(g, h, low_high_theta[1], u)
    x4, y4 = projectile(g, h, theta_max, u)
    x5, y5 = x_bounding, bounding(x_bounding)

    plt.plot(x5, y5,'--', color='magenta', label="Bounding")
    plt.plot(x4, y4,'--', color='red', label="Max Range")
    plt.plot(x3, y3,'-', color='blue', label="High")
    plt.plot(x1, y1,'-', color='lime', label="low")
    plt.plot(x2, y2,'--', color='black', label="Min u")
    plt.plot(X, Y,'*', color='red')
    plt.xlim(0, None)
    plt.ylim(0, None)
    plt.legend()

    plt.xlabel("x /m")
    plt.ylabel("y /m")
    plt.show()

if __name__ == "__main__":
    main()