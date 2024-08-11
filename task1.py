import matplotlib.pyplot as plt
import numpy as np

def main():

    theta, g, u, h = float(input("Angle from horizontal: ")), float(input("Gravity: ")), float(input("Speed: ")), float(input("Height: "))
    theta_rad = np.radians(theta)

    x, y = projectile(g, h, theta_rad, u)

    plt.plot(x, y, marker='o', linestyle='-', color="black", label="No air resistance", markersize=5, markerfacecolor='blue')
    plt.xlabel('x /m')
    plt.ylabel('y above launch height /m')
    plt.title("Projectile motion model")
    plt.ylim(0, None)
    plt.xlim(0, None)   
    plt.grid(True)
    plt.legend()
    plt.show()

def projectile(g, h, theta, v, num=100):

    v_x = v * np.cos(theta)
    v_y = v * np.sin(theta)
    t_flight = (v_y + np.sqrt(v_y**2 + 2 * g * h)) / g

    t = np.linspace(0, t_flight, num=num)
    
    x = v_x * t
    y = h + v_y * t - 0.5 * g * t**2

    return x, y


if __name__ == "__main__":
    main()