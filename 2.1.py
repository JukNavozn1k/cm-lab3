"""1. По таблице с равноотстоящими значениями аргумента вычислить значения функции для заданных значений аргументов, используя первую и вторую интерполяционные формулы Ньютона. Точность E<=0.000001.
Задание:

X1=1,4161; X2=1,4625; X3=1,4135; X4=1,4700;

1,415     0,888551 
1,420     0,889599 
1,425     0,890637 
1,430     0,891667 
1,435     0,892687 
1,440     0,893698 
1,445     0,894700 
1,450     0,895693 
1,455     0,896677 
1,460     0,897653 
1,465     0,898619 

Данная версия считает без учёта точности

"""


def newton_interpolation(x, x_values, y_values):
  n = len(x_values)
  f = y_values.copy() # copy y_values to f
  for i in range(1, n):
    for j in range(n - 1, i - 1, -1):
      f[j] = (f[j] - f[j - 1]) / (x_values[j] - x_values[j - i])
  result = 0.0
  for i in range(n):
    term = f[i]
    for j in range(i):
      term *= (x - x_values[j])
    result += term
  return result

# example usage
x_values = [1.4161, 1.4625, 1.4135, 1.4700]
y_values = [1.415, 1.420, 1.425, 1.430, 1.435, 1.440, 1.445, 1.450, 1.455, 1.460, 1.465]

for x in y_values:
  y = newton_interpolation(x, x_values, y_values)
  print(f'f({x:.4f}) = {y:.6f}')
