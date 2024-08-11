import matplotlib.pyplot as plt
import numpy as np

from task1 import projectile

def main():
    theta, g, u, h = float(input("Angle from horizontal: ")), float(input("Gravity: ")), float(input("Speed: ")), float(input("Height: "))
    theta_rad = np.radians(theta)

    theta_max = np.arcsin(1/np.sqrt(2+(2*g*h)/(u**2)))

    R = u**2/g * (np.sin(theta_rad)*np.cos(theta_rad)+np.cos(theta_rad)*np.sqrt(np.sin(theta_rad)**2+2*g*h/u**2))
    Rmax = u**2/g * np.sqrt(1+2*g*h/u**2)

    T = R/(u*np.cos(theta_rad))
    Tmax = Rmax/(u*np.cos(theta_max))

    x, y = projectile(g, h, theta_rad, u)
    xmax, ymax = projectile(g, h, theta_max, u)

    theta_max_text = 'θ$_{max}$'

    plt.plot(x, y, '-', color="blue", label=f"θ={round(theta, 1)}°. T={round(T, 2)}s.")
    plt.plot(xmax, ymax, '--', color='red', label=f"{theta_max_text}={round(theta_max*180/np.pi, 1)}°. T={round(Tmax, 2)}s.")
    plt.xlabel('x /m')
    plt.ylabel('y /m')
    plt.ylim(0, None)
    plt.xlim(0, None)   
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()