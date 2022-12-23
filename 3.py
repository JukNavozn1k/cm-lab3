import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Data points
x = np.array([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])
y = np.array([0, 5, 9, 13, 17, 20, 24, 26, 29, 32])

# Number of data points
n = len(x)

# Initialize a and b to 0
a = 0
b = 0

# Initialize the RMSE to a large value
RMSE = float('inf')

# Set the tolerance for the RMSE
tolerance = 1e-6

# Set the maximum number of iterations
max_iterations = 100

# Initialize the iteration counter
iteration = 0

# Initialize the table for printing the results
results = []

# Perform the iterations
while RMSE > tolerance and iteration < max_iterations:
    # Initialize the sums
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_xx = 0
    sum_error = 0
    
    # Calculate the sums
    for i in range(n):
        sum_x += x[i]
        sum_y += y[i]
        sum_xy += x[i]*y[i]
        sum_xx += x[i]*x[i]
        sum_error += (y[i] - (a*x[i] + b))**2
    
    # Calculate the estimates for a and b
    a_new = (n*sum_xy - sum_x*sum_y)/(n*sum_xx - sum_x**2)
    b_new = (sum_y - a_new*sum_x)/n
    
    # Calculate the RMSE
    RMSE = np.sqrt(sum_error/n)
    
    # Update the values of a and b
    a = a_new
    b = b_new
    
    # Increment the iteration counter
    iteration += 1
    
    # Add the results to the table
    results.append([iteration, a, b, RMSE])

# Print the results
print(tabulate(results, headers=['Iteration', 'a', 'b', 'RMSE']))
print('Linear dependence Ax + b ')

# Plot the data points and the fitted linear function
plt.plot(x, y, 'o', label='Data points')
plt.plot(x, a*x + b, '-', label='Fitted linear function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

