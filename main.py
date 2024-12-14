import numpy as np
import tkinter as tk
from tkinter import messagebox, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class SOM:
    def __init__(self, grid_size, input_dim, sigma, learning_rate):
        self.grid_size = grid_size
        self.input_dim = input_dim
        self.weights = np.random.rand(grid_size, grid_size, input_dim)
        self.sigma = sigma
        self.learning_rate = learning_rate

        neuron_positions = []
        for i in range(grid_size):
            for j in range(grid_size):
                neuron_positions.append([i, j])
        self.neuron_positions = np.array(neuron_positions)


    def find_bmu(self, input_vector):
        min_distance = float('inf')
        bmu_idx = (0, 0)
        
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                weight_vector = self.weights[i, j]
                distance = 0
                for d in range(self.input_dim):
                    diff = weight_vector[d] - input_vector[d]
                    distance += diff * diff
                distance = distance ** 0.5
                
                if distance < min_distance:
                    min_distance = distance
                    bmu_idx = (i, j)
        return bmu_idx


    def update_weights(self, input_vector, bmu_idx, iteration, max_iterations):
        learning_rate_decay = self.learning_rate * (2.71828 ** (-iteration / max_iterations))  
        sigma_decay = self.sigma * (2.71828 ** (-iteration / max_iterations))

        bmu_x, bmu_y = bmu_idx 

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                distance = ((bmu_x - i) ** 2 + (bmu_y - j) ** 2) ** 0.5 
                neighborhood_influence = (2.71828 ** (-distance ** 2 / (2 * sigma_decay ** 2)))

                for d in range(self.input_dim):
                    weight_difference = input_vector[d] - self.weights[i, j, d]
                    
                    self.weights[i, j, d] += neighborhood_influence * learning_rate_decay * weight_difference
                    
                    

    def train(self, input_vectors, max_epochs):
        for epoch in range(max_epochs):
            for input_vector in input_vectors:
                bmu_idx = self.find_bmu(input_vector)
                self.update_weights(input_vector, bmu_idx, epoch, max_epochs)

def initialize_som(grid_size, sigma, learning_rate, max_epochs, input_vectors=None):
    som = SOM(grid_size, input_dim=3, sigma=sigma, learning_rate=learning_rate)

    if input_vectors is None:
        input_vectors = np.random.randint(0, 256, size=(1000, 3)) / 255.0
    else:
        input_vectors = np.array(input_vectors) / 255.0

        for i in range(grid_size):
            for j in range(grid_size):
                index = (i * grid_size + j) % len(input_vectors)
                som.weights[i, j] = input_vectors[index]

    return som, input_vectors

def train_som(som, input_vectors, max_epochs):
    som.train(input_vectors, max_epochs)
    return som

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Clustering using Kohonen Network")

        self.left_frame = tk.Frame(root)
        self.left_frame.pack(side="left", padx=10, pady=10)

        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side="right", padx=10, pady=10)

        tk.Label(self.right_frame, text="Grid Size:").pack(pady=5)
        self.entry_grid_size = tk.Entry(self.right_frame)
        self.entry_grid_size.pack(pady=5)

        tk.Label(self.right_frame, text="Initial Radius (sigma):").pack(pady=5)
        self.entry_sigma = tk.Entry(self.right_frame)
        self.entry_sigma.pack(pady=5)

        tk.Label(self.right_frame, text="Learning Rate:").pack(pady=5)
        self.entry_learning_rate = tk.Entry(self.right_frame)
        self.entry_learning_rate.pack(pady=5)

        tk.Label(self.right_frame, text="Max Epochs:").pack(pady=5)
        self.entry_max_epochs = tk.Entry(self.right_frame)
        self.entry_max_epochs.pack(pady=5)

        self.use_custom_input = tk.IntVar()
        self.checkbox_custom_input = tk.Checkbutton(self.right_frame, text="Add Custom Input Space", variable=self.use_custom_input)
        self.checkbox_custom_input.pack(pady=10)

        self.btn_input_space = tk.Button(self.right_frame, text="Define Input Space", command=self.define_input_space)
        self.btn_input_space.pack(pady=10)

        self.btn_start = tk.Button(self.right_frame, text="Start Clustering", command=self.start_clustering)
        self.btn_start.pack(pady=10)

        self.btn_repeat_training = tk.Button(self.right_frame, text="Repeat Training", command=self.repeat_training)
        self.btn_repeat_training.pack(pady=10)

        self.canvas_before = None
        self.canvas_after = None
        self.input_vectors = []  
        self.som = None  
        self.colors = None  

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def define_input_space(self):
        num_inputs = simpledialog.askinteger("Input", "Enter number of colors:", minvalue=1)

        if num_inputs:
            self.input_vectors = []
            for i in range(num_inputs):
                color_str = simpledialog.askstring("Input", f"Enter RGB color {i+1} (comma-separated, e.g., 255,0,0 for red):")
                try:
                    color = []
                    for x in color_str.split(','):
                        color.append(int(x.strip()))

                    valid_color = True
                    if len(color) == 3:
                        for x in color:
                            if not (0 <= x <= 255):
                                valid_color = False
                                break
                        if valid_color:
                            self.input_vectors.append(color)
                    
                    else:
                        messagebox.showerror("Invalid Input", "Please enter valid RGB values between 0 and 255.")
                        return
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid RGB values.")
                    return

    def start_clustering(self):
        try:
            grid_size = int(self.entry_grid_size.get())
            sigma = float(self.entry_sigma.get())
            learning_rate = float(self.entry_learning_rate.get())
            max_epochs = int(self.entry_max_epochs.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for grid size, sigma, learning rate, and max epochs.")
            return
        if self.use_custom_input.get() == 1:
            if not self.input_vectors:
                messagebox.showerror("No Input Space", "Please define the input space (colors) before starting clustering.")
                return
            self.som, self.colors = initialize_som(grid_size, sigma, learning_rate, max_epochs, self.input_vectors)
        else:
            self.som, self.colors = initialize_som(grid_size, sigma, learning_rate, max_epochs)

        self.visualize_clustering(self.som, grid_size, "Before Training", "before")
        self.som = train_som(self.som, self.colors, max_epochs)
        self.visualize_clustering(self.som, grid_size, "After Training", "after")

    def repeat_training(self):
        if self.som is None:
            messagebox.showerror("No Training", "Please start clustering before repeating training.")
            return
        try:
            max_epochs = int(self.entry_max_epochs.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for max epochs.")
            return

        self.som = train_som(self.som, self.colors, max_epochs)
        self.visualize_clustering(self.som, int(self.entry_grid_size.get()), "After Re-Training", "after")

    def visualize_clustering(self, som, grid_size, title, stage):
        if stage == "before" and self.canvas_before:
            self.canvas_before.get_tk_widget().destroy()
        elif stage == "after" and self.canvas_after:
            self.canvas_after.get_tk_widget().destroy()

        fig, ax = plt.subplots(figsize=(5, 5))
        ax.axis('off')

        for i in range(grid_size):
            for j in range(grid_size):
                color = som.weights[i, j]
                circle = plt.Circle((i + 0.5, j + 0.5), 0.5, color=color)
                ax.add_artist(circle)

        ax.set_xlim(0, grid_size)
        ax.set_ylim(0, grid_size)
        ax.set_title(title)
        ax.set_aspect('equal')

        if stage == "before":
            self.canvas_before = FigureCanvasTkAgg(fig, master=self.left_frame)
            self.canvas_before.draw()
            self.canvas_before.get_tk_widget().pack(side="left", padx=10)
        elif stage == "after":
            self.canvas_after = FigureCanvasTkAgg(fig, master=self.left_frame)
            self.canvas_after.draw()
            self.canvas_after.get_tk_widget().pack(side="left", padx=10)

    def on_closing(self):
        self.root.quit()
        self.root.destroy()

root = tk.Tk()
app = GUI(root)
root.mainloop()
