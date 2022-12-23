from typing import List, Tuple
from tabulate import tabulate

def interpolate(values: List[Tuple[float, float]], x: float) -> float:
    # Number of pairs of values
    n = len(values)

    # Initialize the array of differences
    differences = [values[i][1] for i in range(n)]
    
    # Calculate the differences using Newton's interpolation formulas
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            differences[i] = (differences[i] - differences[i - 1]) / (values[i][0] - values[i - j][0])
    
    # Print the table of intermediate calculations
    headers = ["i", "x", "f[x]", "differences"]
    table = []
    for i in range(n):
        row = [i, values[i][0], values[i][1], differences[i]]
        table.append(row)
    print(tabulate(table, headers))
    
    # Calculate the interpolated value
    result = differences[n - 1]
    for i in range(n - 2, -1, -1):
        result = result * (x - values[i][0]) + differences[i]
    
    return result

# Test the interpolate function
values = [(1.415, 0.888551), (1.420, 0.889599), (1.425, 0.890637), (1.430, 0.891667), 
          (1.435, 0.892687), (1.440, 0.893698), (1.445, 0.894700), (1.450, 0.895693), 
          (1.455, 0.896677), (1.460, 0.897653), (1.465, 0.898619)]

x_values = [1.4161, 1.4625, 1.4135, 1.4700]

for x in x_values:
    print(f"Interpolated value at x={x}: {interpolate(values, x)}")
