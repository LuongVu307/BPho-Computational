import matplotlib.pyplot as plt
import numpy as np
def main():
    g, u = float(input("g: ")), float(input("u: "))
    t = np.linspace(0, 3*u/(2*g) * (np.sin(np.radians(85)) + np.sqrt(round(np.sin(np.radians(85))**2-8/9, 2)))*1.2, 100)
    plt.figure(figsize=(10, 8))
    theta_list = [30, 45, 60, 70.5, 78, 85]
    for theta in theta_list:
        theta_rad = np.radians(theta)
        cal_r = lambda t : np.sqrt(u**2*t**2-g*t**3*u*np.sin(theta_rad)+1/4*g**2*t**4)
        if theta >= 70.5:
            t_max = 3*u/(2*g) * (np.sin(theta_rad) - np.sqrt(round(np.sin(theta_rad)**2-8/9, 2)))
            t_min = 3*u/(2*g) * (np.sin(theta_rad) + np.sqrt(round(np.sin(theta_rad)**2-8/9, 2)))
            plt.plot(t_max, cal_r(t_max), "*", color="magenta")
            plt.plot(t_min, cal_r(t_min), "*", color="darkblue")

        x1, y1 = t, cal_r(t)
        plt.plot(x1, y1, "-", label = f"θ = {theta}°")
    plt.xlabel('t /s')
    plt.ylabel('range /m')
    plt.grid(True)
    plt.ylim(0, None)
    plt.xlim(0, None)
    plt.legend()
    plt.figure(figsize=(10, 8))
    cal_xy = lambda t : (u* np.cos(theta_rad) * t, u * np.sin(theta_rad) * t - 0.5 * g * t**2) 
    list_y = []
    for theta in theta_list:
        theta_rad = np.radians(theta)
        if theta >= 70.5:
            t_max = 3*u/(2*g) * (np.sin(theta_rad) - np.sqrt(round(np.sin(theta_rad)**2-8/9, 2)))
            t_min = 3*u/(2*g) * (np.sin(theta_rad) + np.sqrt(round(np.sin(theta_rad)**2-8/9, 2)))

            plt.plot(cal_xy(t_max)[0], cal_xy(t_max)[1], "*", color="magenta")
            plt.plot(cal_xy(t_min)[0], cal_xy(t_min)[1], "*", color="darkblue")
        x1, y1 = cal_xy(t)
        list_y.append(y1[-1])
        plt.plot(x1, y1, "-", label = f"θ = {theta}°")
    plt.xlabel('x /m')
    plt.ylabel('y /m')
    plt.ylim(max(list_y), None)
    plt.xlim(0, None)
    plt.grid(True)
    plt.legend()   
    plt.show()
if __name__ == "__main__":
    main()