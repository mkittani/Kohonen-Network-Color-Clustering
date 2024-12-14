# Kohonen Network Color Clustering

Welcome to the **Kohonen Network Color Clustering** project! This project demonstrates how to apply a Kohonen Self-Organizing Map (SOM) to cluster colors using an unsupervised machine learning approach. With this tool, you can train **(without any training built-in methods)** an SOM on a custom set of colors or let the program generate random colors for you. The application provides an interactive GUI for configuring the network and visualizing the clustering process before and after training.

## Features 🚀

- **Interactive GUI**: Configure the SOM parameters using a user-friendly gui interface built with Tkinter.
- **Customizable Settings**: 
  - Choose the grid size for the SOM.
  - Set the initial radius (`sigma`) and learning rate.
  - Define the maximum number of epochs for training.
- **Custom Input Space Configuration**: 
  - Add custom RGB colors as input vectors or let the system generate random colors.
  - Define up to 1000 custom colors for clustering.
- **Visualization**: See the clustering results in real-time with visual representations of the grid before and after training.
- **Repeat Training**: Restart the training process to refine the clustering and adjust parameters as needed.

## How It Works

1. **Initial Setup**:
   - Set up a grid for the SOM where each neuron represents a color.
   - Initialize the grid with random colors (or custom colors if defined by the user).

2. **Training**:
   - The SOM learns to cluster the input colors by adjusting the weights of the neurons based on their similarity to the input vectors.
   - As the training progresses, the SOM adjusts its internal representation of the color space, organizing similar colors together.

3. **Visualization**:
   - The GUI displays two grids: one before training and one after training. This allows you to see how the SOM has grouped the colors.
   - The colors of each neuron are visualized as circles on the grid.

## Requirements 📦

Before you start, make sure you have the following Python packages installed:

- `numpy`
- `matplotlib`
- `tkinter`

You can install the required dependencies using the following command:

```bash
pip install numpy matplotlib
```
## Installation 
1. Clone the repository:
   ```bash
   git clone https://github.com/mkittani/Kohonen-Network-Color-Clustering.git
2. Ru the application:
   ```bash
   python main.py

## GUI Instructions 📊

### 1. **Set Grid Size**  
   - Enter the desired grid size for the SOM (Self-Organizing Map). For example, you can enter `10` for a 10x10 grid.  
   - The grid size determines the number of neurons in the SOM. A larger grid provides more neurons to map the input colors but may require more time to train.

### 2. **Define Parameters**  
   - **Sigma (Initial Radius)**:  
     This parameter controls the influence of the "winner" neuron (the neuron most similar to the input color) on its neighboring neurons. A higher value means a larger neighborhood will be affected by the winner, which allows for broader changes in the grid. A lower value makes the influence more localized.
   - **Learning Rate**:  
     The learning rate defines how much the weights of the neurons should be adjusted during each training step. A higher learning rate will cause the network to learn faster, but it can also make the learning process unstable. A lower learning rate results in more gradual learning.
   - **Max Epochs**:  
     Set the maximum number of training iterations (epochs). Each epoch consists of one full pass through the input colors. Increasing the number of epochs allows the SOM more opportunities to fine-tune the weights.

### 3. **Input Space**  
   - Use the checkbox to enable the option to define custom input colors. When enabled:
     - You can define the colors by entering RGB values (e.g., `255,0,0` for red).
     - A pop-up will prompt you to enter the number of colors and their RGB values. You can add as many as you like, ensuring each RGB value is between `0` and `255`.
   - If you don't want to define custom colors, simply leave the checkbox unchecked. The system will automatically generate random colors for training the SOM.

### 4. **Start Clustering**  
   - After setting the grid size, parameters, and input colors, click the **Start Clustering** button to begin training the SOM.
   - During the training process, the system will adjust the weights of the neurons based on the input colors. After training, the grid will update to display the clustering results.
   - The visualization will show a grid of circles, each representing a neuron. The color of each circle corresponds to the neuron's weight, which has been adjusted during training.

### 5. **Repeat Training**  
   - If you would like to refine the clustering results, you can adjust the parameters (grid size, sigma, learning rate, or max epochs) and click the **Repeat Training** button.
   - This will retrain the SOM with the new settings and update the visualization to show how the grid has changed.

