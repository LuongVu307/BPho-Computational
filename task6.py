import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt
from task1 import projectile    

def main():
    theta, g, u, h = float(input("Angle from horizontal: ")), float(input("Gravity: ")), float(input("Speed: ")), float(input("Height: "))
    theta_rad = np.radians(theta)
    theta_max = np.arcsin(1/np.sqrt(2+(2*g*h)/(u**2)))

    R = u**2/g * (np.sin(theta_rad)*np.cos(theta_rad)+np.cos(theta_rad)*np.sqrt(np.sin(theta_rad)**2+2*g*h/u**2))
    Rmax = u**2/g * np.sqrt(1+2*g*h/u**2)
    T = R/(u*np.cos(theta_rad))
    Tmax = Rmax/(u*np.cos(theta_max))

    x, y = projectile(g, h, theta_rad, u, num=int(T*100))
    xmax, ymax = projectile(g, h, theta_max, u, num=int(Tmax*100))
    s = 0
    smax = 0
    distance = lambda x1, x2, y1, y2 : sqrt((x2 - x1)**2 + (y2 - y1)**2)
    for i, j in zip(range(len(x)-1), range(len(y)-1)):
        s += distance (x[i], x[i+1], y[j], y[j+1])
    for i, j in zip(range(len(xmax)-1), range(len(ymax)-1)):
        smax += distance (xmax[i], xmax[i+1], ymax[j], ymax[j+1])

    theta_max_text = 'θ$_{max}$'
    s_max_text = 's$_{max}$'

    plt.plot(x, y, '-', color="blue", label=f"θ={round(theta, 1)}°. T={round(T, 2)}s. s={round(s, 2)}")
    plt.plot(xmax, ymax, '--', color='red', label=f"{theta_max_text}={round(theta_max*180/np.pi, 1)}°. T={round(Tmax, 2)}s. {s_max_text}={round(smax, 2)}")
    plt.xlabel('x /m')
    plt.ylabel('y /m')
    plt.ylim(0, None)
    plt.xlim(0, None)   
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()