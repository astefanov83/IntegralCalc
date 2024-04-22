import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
    grapher("x**2")

if __name__ == '__main__':
    main()
