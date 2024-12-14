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

## How to Work

### 1. **Set Grid Size**  
   - Enter the desired grid size for the SOM (Self-Organizing Map). For example, you can enter `10` for a 10x10 grid.  
   - The grid size determines the number of neurons in the SOM. A larger grid provides more neurons to map the input colors but may require more time to train.

### 2. **Define Parameters**  
   - **Sigma (Initial Radius)**:  
     This parameter controls the influence of the "winner" neuron (the neuron most similar to the input color) on its neighboring neurons. A higher value means a larger neighborhood will be affected by the winner, which allows for broader changes in the grid. A lower value makes the influence more localized.
   - **Learning Rate**:  
     ***MUST BE BETWEEN 0 AND 1.*** It defines how much the weights of the neurons should be adjusted during each training step. A higher learning rate will cause the network to learn faster, but it can also make the learning process unstable. A lower learning rate results in more gradual learning.
   - **Max Epochs**:  
     Set the maximum number of training iterations (epochs). Each epoch consists of one full pass through the input colors. Increasing the number of epochs allows the SOM more opportunities to fine-tune the weights.

### 3. **Input Space**  
   - Use the checkbox to enable the option to define custom input colors. When enabled:
   - If you don't want to define custom colors, simply leave the checkbox unchecked. The system will automatically generate random colors for training the SOM.

### 4. **Start Clustering**  
   - After setting the grid size, parameters, and input colors, click the **Start Clustering** button to begin training the SOM.
   - During the training process, the system will adjust the weights of the neurons based on the input colors. After training, the grid will update to display the clustering results.
   - The visualization will show a grid of circles, each representing a neuron. The color of each circle corresponds to the neuron's weight, which has been adjusted during training.

### 5. **Repeat Training**  
   - If you would like to refine the clustering results, click the **Repeat Training** button.
   - This will retrain the SOM and update the visualization to show how the grid has changed.

