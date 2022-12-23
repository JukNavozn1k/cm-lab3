from tabulate import tabulate

def interpolate(x_values, f_values, x):
    weights = []
    for i, x_i in enumerate(x_values):
        weight = 1
        for j, x_j in enumerate(x_values):
            if i != j:
                weight *= (x - x_j) / (x_i - x_j)
        weights.append(weight)

    # Initialize empty table for storing calculations
    table = []
    for w, f in zip(weights, f_values):
        # Calculate intermediate product and append to table
        product = w * f
        table.append((w, f, product))
    interpolated_value = sum(w * f for w, f in zip(weights, f_values))
    return interpolated_value, table

x_values = [0.43, 0.48, 0.55, 0.62, 0.70, 0.75]
f_values = [1.63597, 1.73234, 1.87686, 2.03345, 2.22846, 2.83973]
x = 0.702
interpolated_value, table = interpolate(x_values, f_values, x)


# Print table of calculations using tabulate library
headers = ["Weight", "Function Value", "Intermediate Product"]
print(tabulate(table, headers=headers))
print('Interpolation value at x = 0.702: ',interpolated_value)