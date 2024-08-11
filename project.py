import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import numpy as np


def main():
    root = tk.Tk()
    root.title("Basic Tkfloater Window")
    root.geometry("600x500")  # Width x Height in pixels

    def create_box(x, y, text, width, height):
        box_frame = tk.Frame(root, width=width, height=height, bg='white', borderwidth=2, relief='solid')
        box_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its content
        box_frame.place(x=x, y=y)

        number_label = tk.Label(box_frame, text=text, font=("Arial", 16), bg='white')
        number_label.pack(expand=True)

        return number_label

    def create_slider(orient='horizontal', start=0, end=100, x=0, y=0, width=200, length=50, x_label=0, 
                    y_label=0, initial_val="", resolution=1):
        def update_label(value):
            if len(value) == 5:
                value = value[:-1]
            label.config(text=f"{value}")
            # label.place(x=10, y=10)
        
        frame = tk.Frame(root, width=width, height=length)
        frame.place(x=x+width/2, y=y)
        
        scale = tk.Scale(frame, from_=start, to=end, orient=orient, command=update_label, 
                        width=width, length=length, resolution=resolution, showvalue=False, 
                        sliderlength=20)
        scale.pack()
        scale.place(x=0, y=0)

        if initial_val:
            scale.set(initial_val)

        label = create_box(x_label, y_label, scale.get(), 50, 30)
        # update_label(scale.get())


        return scale

    def create_entry(width=20, height=1, x=0, y=0, initial_val=""):
        entry = tk.Entry(root, width=width, font=("Arial", 10))
        entry.place(x=x, y=y, height=height)
        if initial_val:
            entry.insert(1, initial_val)

        return entry

    def create_label(text, x, y, font=("Arial", 12), fg="black"):
        label = tk.Label(root, text=text, font=font, fg=fg)
        label.place(x=x, y=y)
        return label

    def create_data(h, u, theta, m, g, drag, S, D):
        theta_rad = np.radians(theta)

        k = 1/2 * drag*D*S/m
        ux, uy = u*np.cos(theta_rad), u*np.sin(theta_rad)


        X, Y = [0], [h]
        vx, vy = ux, uy
        v = np.sqrt(vx**2 + vy**2)
        x, y = 0, h
        T1 = 0

        X_no_resistance, Y_no_resistance = [0], [h]
        vx_no_resistance, vy_no_resistance = ux, uy
        x_no_resistance, y_no_resistance = 0, h
        T2 = 0


        dt = 0.01
        while y >= 0 or y_no_resistance >= 0:

            if y >= 0:

                ax = -k * (vx/v) * v**2
                ay = -g - k * (vy/v) * v**2

                x += vx * dt + 0.5 * ax * dt**2
                y += vy * dt + 0.5 * ay * dt**2

                vx += ax * dt
                vy += ay * dt

                X.append(x)
                Y.append(y)
                T1 += dt

            if y_no_resistance >= 0:
                x_no_resistance += vx_no_resistance*dt
                y_no_resistance += vy_no_resistance*dt

                vy_no_resistance += -g*dt
                
                X_no_resistance.append(x_no_resistance)
                Y_no_resistance.append(y_no_resistance)

                T2 += dt

        bounding = lambda x : u**2/(2*g) - g/(2*u**2)*x**2 + h
        X_bounding, Y_bounding = [0], [u**2/(2*g)]
        x_bounding, y_bounding = 0, u**2/(2*g)

        # print(x_no_resistance)

        if theta != 90:
            dx = x_no_resistance/100
            while y_bounding >= 0:
                x_bounding += dx
                # print(x_bounding, y_bounding)

                y_bounding = bounding(x_bounding)
                X_bounding.append(x_bounding)
                Y_bounding.append(y_bounding)

                
        # print(y_bounding)
        return (X, Y, "drag", x, T1, np.linspace(0, T1, len(X))), (X_no_resistance, Y_no_resistance, "no drag", x_no_resistance, T2,
                                                                    np.linspace(0, T2, len(X_no_resistance))), (X_bounding, Y_bounding, "_", None, None, [])

    class GraphApp:
        def __init__(self, root, datas, x_coord, y_coord, width, height):
            self.root = root
            self.datas = datas
            self.width = width
            self.height = height
            self.plot_type = "y vs x"
            
            # Create a frame within the parent
            self.frame = tk.Frame(root, width=width + x_coord, height=height + y_coord)
            self.frame.place(x=x_coord, y=y_coord)
            
            # Create a figure for the plot
            self.fig = Figure(figsize=(round(width / 100), round(height / 100)), dpi=100)
            self.ax = self.fig.add_subplot(111)
            
            # Create a canvas to display the plot
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            self.plot_data(datas)

        def plot_data(self, datas):
            self.ax.clear()  # Clear the current plot
            for data in datas:
                if self.plot_type == "y vs x":
                    self.ax.plot(data[0], data[1], marker='o', markersize=1, linestyle='', label=data[2])
                elif self.plot_type == "y vs t":
                    if list(data[5]):
                        self.ax.plot(data[5], data[1], marker='o', markersize=1, linestyle='', label=data[2])
                elif self.plot_type == "x vs t":
                    if list(data[5]):
                        self.ax.plot(data[5], data[0], marker='o', markersize=1, linestyle='', label=data[2])

            self.ax.set_ylim(0, None)
            self.ax.set_xlim(0, None)
            self.ax.legend(fontsize="small")
            self.ax.grid(True)
            self.canvas.draw()

        def update_graph(self, new_datas, plot_type):
            self.datas = new_datas
            self.plot_type = plot_type
            self.plot_data(new_datas)

    def save_plot(name_file, datas, plot_type):
        plt.figure(figsize=(10, 8))
        for data in datas:
            if plot_type == "y vs x":
                plt.plot(data[0], data[1], marker='o', markersize=1, linestyle='', label=data[2])
                plt.xlabel('x (m)', fontsize=14)
                plt.ylabel('y (m)', fontsize=14)

            elif plot_type == "y vs t":
                if list(data[5]):
                    plt.plot(data[5], data[1], marker='o', markersize=1, linestyle='', label=data[2])
                plt.xlabel('t (s)', fontsize=14)
                plt.ylabel('y (m)', fontsize=14)

            elif plot_type == "x vs t":
                if list(data[5]):
                    plt.plot(data[5], data[0], marker='o', markersize=1, linestyle='', label=data[2])
                plt.xlabel('t (s)', fontsize=14)
                plt.ylabel('x (m)', fontsize=14)


        plt.ylim(0, None)
        plt.xlim(0, None)
        plt.legend()
        plt.grid(True)

        plt.savefig(f'saved_graph/{name_file}.png', dpi=800)

    def update_all(graphapp, h, u, theta, m, g, drag, S, D, plot_type):

        h_val, u_val, theta_val, m_val, g_val, drag_val, S_val, D_val = float(h.get()), float(u.get()), float(theta.get()), float(m.get()), float(g.get()), 
        float(drag.get()), float(S.get()), float(D.get())

        data1, data2, data3 = create_data(h_val, u_val, theta_val, m_val, g_val, drag_val, S_val, D_val)

        update_entry(range, round(data2[3], 4))
        update_entry(time_flight, round(data2[4], 4))
        update_entry(range_drag, round(data1[3], 4))
        update_entry(time_flight_drag, round(data1[4], 4))


        graphapp.update_graph([data1, data2, data3], plot_type)

    def update_entry(entry, new_text):
        entry.config(state='normal')  # Allow modifying the entry
        entry.delete(0, tk.END)       # Clear the current content
        entry.insert(0, new_text)     # Insert the new content
        entry.config(state='readonly')


    create_box(360, 40, 50, 50, 30)
    create_box(420, 40, 100, 50, 30)
    create_box(480, 40, 90, 50, 30)
    create_box(540, 40, 3, 50, 30)

    h = create_slider("vertical", 50, 0, x=335, y=125, width=50, length=250, x_label=360, y_label=90, 
                    resolution=0.1)
    u = create_slider("vertical", 100, 0, x=395, y=125, width=50, length=250, x_label=420, y_label=90, 
                    resolution=0.1)
    theta = create_slider("vertical", 90, 0, x=455, y=125, width=50, length=250, x_label=480, y_label=90, 
                        resolution=0.1)
    m = create_slider("vertical", 3, 0.01, x=515, y=125, width=50, length=250, x_label=540, y_label=90, 
                    resolution=0.01)


    create_label("g (ms^-2)", 22, 273, ("Arial", 8, "bold"), "green")
    create_label(f"          Drag\ncoefficient", 15, 308, ("Arial", 8, "bold"), "green")
    create_label("A (m^2)", 30, 353, ("Arial", 8, "bold"), "green")
    create_label(f"Air Density\n (kgm^-3)", 15, 387, ("Arial", 8, "bold"), "green")


    create_label(f"Range\n(No Drag) (m)", 165, 270, ("Arial", 8, "bold"), "red")
    create_label(f"Time of flight /s \n (No Drag)", 158, 308, ("Arial", 8, "bold"), "red")
    create_label(f"Range\n(Drag) (m)", 180, 350, ("Arial", 8, "bold"), "blue")
    create_label(f"Time of flight /s \n (Drag)", 158, 387, ("Arial", 8, "bold"), "blue")

    create_label(f"h (m)", 370, 70, ("Arial", 8, "bold"), "green")
    create_label(f"u (m/s)", 420, 70, ("Arial", 8, "bold"), "green")
    create_label(f"theta (deg)", 470, 70, ("Arial", 8, "bold"), "green")
    create_label(f"m (kg)", 545, 70, ("Arial", 8, "bold"), "green")

    create_label(f"hmax (m)", 360, 15, ("Arial", 8), "black")
    create_label(f"umax\n(m/s)", 430, 5, ("Arial", 8), "black")
    create_label(f"thetamax\n(deg)", 480, 5, ("Arial", 8), "black")
    create_label(f"mmax\n(kg)", 555, 5, ("Arial", 8), "black")


    g = create_entry(8, 30, 90, 270)
    drag = create_entry(8, 30, 90, 310)
    S = create_entry(8, 30, 90, 350)
    D = create_entry(8, 30, 90, 390)

    if not h.get():
        h = create_slider("vertical", 50, 0, x=335, y=125, width=50, length=250, x_label=360, y_label=90, 
                        resolution=0.1, initial_val="2")
    if not u.get():
        u = create_slider("vertical", 100, 0, x=395, y=125, width=50, length=250, x_label=420, y_label=90,
                        resolution=0.1, initial_val="10")
    if not theta.get():
        theta = create_slider("vertical", 90, 0, x=455, y=125, width=50, length=250, x_label=480, y_label=90, 
                            resolution=0.1, initial_val="45")
    if not m.get():
        m = create_slider("vertical", 5, 0, x=515, y=125, width=50, length=250, x_label=540, y_label=90, 
                        resolution=0.01, initial_val="0.01")
        
    if not g.get():
        g = create_entry(8, 30, 90, 270, initial_val="9.81")
    if not drag.get():
        drag = create_entry(8, 30, 90, 310, initial_val="0.3")
    if not S.get():
        S = create_entry(8, 30, 90, 350, initial_val="0.002")
    if not D.get():
        D = create_entry(8, 30, 90, 390, initial_val="1")

    h_val, u_val, theta_val, m_val, g_val, drag_val, S_val, D_val = float(h.get()), float(u.get()), float(theta.get()), float(m.get()), float(g.get()), 
    float(drag.get()), float(S.get()), float(D.get())
    data1, data2, data3 = create_data(h_val, u_val, theta_val, m_val, g_val, drag_val, S_val, D_val)
    graphapp = GraphApp(root, [data1, data2, data3], x_coord=20, y_coord=35, width=320, height=180)

    button = tk.Button(root, text="Generate graph", command=lambda : update_all(graphapp, h, u, theta, m, g, drag, S, D, plot_type.get()))
    button.pack()
    button.place(x=30, y=450)
    enter_text = tk.Label(root, text="or Press 'Enter'")
    enter_text.place(x=125, y=452)

    root.bind('<Return>', lambda x : update_all(graphapp, h, u, theta, m, g, drag, S, D, plot_type.get()))

    range = create_entry(10, 30, 250, 270)
    time_flight = create_entry(10, 30, 250, 310)
    range_drag = create_entry(10, 30, 250, 350)
    time_flight_drag = create_entry(10, 30, 250, 390)

    update_entry(range, round(data2[3], 4))
    update_entry(time_flight, round(data2[4], 4))
    update_entry(range_drag, round(data1[3], 4))
    update_entry(time_flight_drag, round(data1[4], 4))

    create_label("Type: ", 390, 400, font=("Arial", 10))
    plot_type = ttk.Combobox(root, values=["y vs x", "y vs t", "x vs t"], state="readonly")
    plot_type.pack(padx=10, pady=10)
    plot_type.place(x=430, y=400)
    plot_type.set("y vs x")
    create_label("Name: ", 220, 430, font=("Arial", 10))
    name_file = create_entry(15, 25, 265, 430, "plot1")

    button = tk.Button(root, text="Save .PNG", command=lambda : save_plot(name_file.get(), [data1, data2, data3], plot_type.get()))
    button.pack()
    button.place(x=250, y=460)
    root.mainloop()

if __name__ == "__main__":
    main()