import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
# Given data
x = np.array([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])
y = np.array([0, 5, 9, 13, 17, 20, 24, 26, 29, 32])

# Fit a polynomial of degree 2 to the data
coefficients, residuals, _, _, _ = np.polyfit(x, y, 2, full=True)

# Calculate the root mean square error
rmse = np.sqrt(residuals[0] / len(x))



# Generate prediction points and fit curve
prediction_x = np.linspace(x.min(), x.max(), 100)
prediction_y = np.polyval(coefficients, prediction_x)

# Print a table of the original data and the predicted values
headers = ['x', 'y', 'Predicted y']
data = []
for xx, yy, yy_pred in zip(x, y, np.polyval(coefficients, x)):
    data.append([xx, yy, yy_pred])
print(tabulate(data, headers=headers))
print('Quadratic dependence')
# Print the results
print(f'Root mean square error: {rmse:.2f}')
print(f'Coefficients: {coefficients}')

# Fit a polynomial of degree 2 to the data
coefficients, residuals, _, _, _ = np.polyfit(x, y, 2, full=True)

# Calculate the root mean square error
rmse = np.sqrt(residuals[0] / len(x))

# Generate prediction points and fit curve
prediction_x = np.linspace(x.min(), x.max(), 100)
prediction_y = np.polyval(coefficients, prediction_x)

# Plot the original data and the fitted curve
plt.plot(x, y, 'o', label='Original data')
plt.plot(prediction_x, prediction_y, '-', label='Fitted curve')
plt.legend()
plt.show()