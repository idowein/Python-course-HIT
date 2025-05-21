# %%
import numpy as np

def PearsonCorrelation(X, Y):
    # Calculate the mean of X and Y
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    
    # Calculate the numerator: sum of (xi - mean_X) * (yi - mean_Y)
    numerator = np.sum((X - mean_X) * (Y - mean_Y)) # in hebrew: "MONE"
    
    # Calculate the denominator: sqrt(sum of (xi - mean_X)^2 * sum of (yi - mean_Y)^2)
    denominator = np.sqrt(np.sum((X - mean_X)**2) * np.sum((Y - mean_Y)**2)) # in hebrew: "MECHANE"

    # Return the relation between numerator to denominator
    R = numerator / denominator
    
    # Return the Pearson correlation coefficient
    return R

# %%
# Example usage:
X1 = np.array([9, 7, 5, 3, 1])
Y1 = np.array([10, 6, 1, 5, 3])
R1 = PearsonCorrelation(X1, Y1)
print('R1: {:.14f}'.format(R1))

X2 = np.array([1, 0, 1])
Y2 = np.array([0, 2, 1])
R2 = PearsonCorrelation(X2, Y2)
print('R2: {:.14f}'.format(R2))

# %%
import numpy as np
import matplotlib.pyplot as plt

def PlotFun(t, title):
    # Calculate the two functions
    y1 = 5 * np.sin(t) + 3
    y2 = np.sin(t) + np.cos(t)

    # Plot the first function
    plt.plot(t, y1, label='y1 = 5sin(t) + 3', color='cyan')  # Set color to red and label for the legend
    
    # Plot the second function
    plt.plot(t, y2, label='y2 = sin(t) + cos(t)', color='cyan')  # Set color to blue and label for the legend
    
    # Add a title to the graph
    plt.title(title)
    
    # Add a legend to describe the plots
    plt.legend()
    
    # Add labels to the axes
    plt.xlabel('Time (t)')
    plt.ylabel('Function values')
    
    # Display the plot
    plt.show()

# %%
# Example usage:
# Create a time vector t
t = np.linspace(0, 10, 500)  # 500 points between 0 and 10

# Create graph title
title = "Mathematical Function Plots"

# Call the PlotFun function to plot the graphs
PlotFun(t, title)


