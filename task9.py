import matplotlib.pyplot as plt
import numpy as np
def main():
    theta, u, h, g = float(input("Launch angle: ")), float(input("Launch speed: ")), float(input("Launch height: ")), float(input("g: "))
    drag, S, D, m = float(input("Drag coefficient: ")), float(input("Cross sectional area: ")), float(input("Air density: ")), float(input("Object mass: "))
    theta_rad = np.radians(theta)
    k = 1/2 * drag*D*S/m
    ux, uy = u*np.cos(theta_rad), u*np.sin(theta_rad)
    X, Y = [0], [h]
    vx, vy = ux, uy
    v = u
    x, y = 0, h
    X_no_resistance, Y_no_resistance = [0], [h]
    vx_no_resistance, vy_no_resistance = ux, uy
    x_no_resistance, y_no_resistance = 0, h
    dt = 0.01
    while True:
        ax = -vx/v *k*(v**2)
        ay = -g -vy/v*k*(v**2)
        x += vx * dt + 1/2 * ax * dt**2
        y += vy * dt + 1/2 * ay * dt**2
        vx += ax * dt
        vy += ay * dt
        X.append(x)
        Y.append(y)
        x_no_resistance += vx_no_resistance*dt 
        y_no_resistance += vy_no_resistance*dt -  1/2 * g * dt**2

        vy_no_resistance += -g*dt
        
        X_no_resistance.append(x_no_resistance)
        Y_no_resistance.append(y_no_resistance)

        if y <= 0 and y_no_resistance <= 0:
            break
    plt.plot(X, Y, marker='o', markersize=2,  color="red", linestyle='', label="Drag")
    plt.plot(X_no_resistance, Y_no_resistance, marker='o', markersize=2, color="blue", linestyle='', label="No Drag")
    plt.title('Projectile motion model')
    plt.xlabel('x /m')
    plt.ylabel('y above launch height /m')
    plt.ylim(0, None)
    plt.xlim(0, None)   
    plt.grid(True)
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()