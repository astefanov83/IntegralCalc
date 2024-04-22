import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def input_page():
    root = tk.Tk()
    root.title("Integral Calculator")

    # Create a frame for the input fields
    frame = tk.Frame(root)
    frame.pack()

    # Create an entry widget for the function
    func_label = tk.Label(frame, text="Enter your function f(x):")
    print(func_label)
    func_label.pack(pady=5)
    func_entry = tk.Entry(frame)
    func_entry.pack(pady=5)

    # Create an entry widget for the lower bound
    x1_label = tk.Label(frame, text="Enter the lower bound of the integral:")
    x1_label.pack(pady=5)
    x1_entry = tk.Entry(frame)
    x1_entry.pack(pady=5)

    # Create an entry widget for the upper bound
    x2_label = tk.Label(frame, text="Enter the upper bound of the integral:")
    x2_label.pack(pady=5)
    x2_entry = tk.Entry(frame)
    x2_entry.pack(pady=5)

    # Create a button to calculate the integral
    button = tk.Button(root, text="Calculate Integral", command=root.quit)
    button.pack(pady=5)

    # Start the Tkinter event loop
    tk.mainloop()

    return func_entry.get(), x1_entry.get(), x2_entry.get()

def grapher(func1):

    def plot_graph():
        try:
            # Get the function from the entry widget
            function = func1

            # Create an array of x values
            x = np.linspace(-10, 10, 100)

            # Evaluate the function for each x value
            y = eval(function)

            # Clear previous plot
            ax.clear()

            # Plot the graph
            ax.plot(x, y)
            ax.axhline(0, color='black',linewidth=0.5)
            ax.axvline(0, color='black',linewidth=0.5)
            ax.set_title('Graph of ' + function)
            ax.grid(True)
            canvas.draw()

        except Exception as e:
            # Display error message if the function is invalid
            messagebox.showerror("Error", str(e))

    # Create the main window
    root = tk.Tk()
    root.title("Function Grapher")

    # Create a frame for the plot
    frame = tk.Frame(root)
    frame.pack()

    # Create an entry widget for the function

    # Create a button to plot the graph
    button = tk.Button(root, text="Plot Graph", command=plot_graph)
    button.pack(pady=5)

    # Create a figure and axis for the plot
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack()

    # Start the Tkinter event loop
    tk.mainloop()

def main():
    inpt, lo, hi = input_page()
    print(inpt)
    grapher(str(inpt))

if __name__ == '__main__':
    main()
