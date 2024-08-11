import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def main():
    theta, g, u, h, C, bounce = float(input("Angle from horizontal: ")), float(input("Gravity: ")), float(input("Speed: ")), float(input("Height: ")),
    float(input("Coefficient: ")), int(input("Stop after: "))
    dt = 0.15
    theta_rad = np.radians(theta)
    x = 0
    y = h
    y_initial = y
    vx = u * np.cos(theta_rad)
    vy = u * np.sin(theta_rad)
    R = u**2/g * (np.sin(theta_rad)*np.cos(theta_rad)+np.cos(theta_rad)*np.sqrt(np.sin(theta_rad)**2+2*g*h/u**2))
    x_path = [x]
    y_path = [y]
    def update(frame):
        nonlocal x, y, vx, vy, dt, bounce, C, x_path, y_path, g
        x_new = x + vx * dt
        y_new = y + vy*dt -0.5*g*dt**2
        vx = vx
        vy -= g*dt
        if y_new <= 0:
            y_new = 0
            vy = -vy * C 
            bounce -= 1
        x, y = x_new, y_new
        x_path.append(x)
        y_path.append(y)
        
        ball.set_data(x, y)
        ball_star.set_data(x, y)
        path.set_data(x_path, y_path)
        if bounce == 0:
            ani.event_source.stop()
        return ball, path, ball_star,
    fig, ax = plt.subplots()
    ax.set_xlim(0, R*(bounce**C+2))
    print(round(theta_rad))
    ax.set_ylim(0, y_initial*1.2*(round(theta_rad+0.5)))
    ball, = ax.plot([], [], 'o', markersize=15, color="lime")
    ball_star, = ax.plot([], [], '*', color="red")
    path, = ax.plot([], [], '-', color="red")
    ani = FuncAnimation(fig, update, frames=np.arange(0, 90), interval=30)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bouncing Ball Animation')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()