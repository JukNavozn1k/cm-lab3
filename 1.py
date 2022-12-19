'''
1. По таблице с неравноотстоящими значениями аргумента выполнить интерполяцию, используя формулу Лагранжа. Точность E<=0,000001.
Задание:

 X=0,702

 0,43     1,63597 
 0,48     1,73234 
 0,55     1,87686 
 0,62     2,03345 
 0,70     2,22846 
 0,75     2,83973 

'''

def lagrange_interpolation(x_values, y_values, x, epsilon=1e-6):
  result = 0
  prev_result = 0
  while True:
    for i in range(len(x_values)):
      L_i = y_values[i]
      for j in range(len(x_values)):
        if i != j:
          L_i *= (x - x_values[j]) / (x_values[i] - x_values[j])
      result += L_i
    if abs(result - prev_result) <= epsilon:
      break
    prev_result = result
    result = 0
  return result

x_values = [0.43, 0.48, 0.55, 0.62, 0.70, 0.75]
y_values = [1.63597, 1.73234, 1.87686, 2.03345, 2.22846, 2.83973]
x = 0.702

interpolated_y = lagrange_interpolation(x_values, y_values, x)
print(interpolated_y)
