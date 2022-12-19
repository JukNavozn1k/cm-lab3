"""
3. По заданным экспериментальным точкам выбрать вид эмпирической зависимости и выполнить среднеквадратичное приближение функции, применив метод наименьших квадратов для оценки параметров выбранной зависимости.
Задание:

1,0        0      
1,1        5      
1,2        9      
1,3        13     
1,4        17     
1,5        20     
1,6        24     
1,7        26     
1,8        29     
1,9        32


"""

from math import sqrt

# define the data points
x = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
y = [0, 5, 9, 13, 17, 20, 24, 26, 29, 32]

# calculate the sums
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum([x[i]*y[i] for i in range(len(x))])
sum_xx = sum([x[i]**2 for i in range(len(x))])
sum_yy = sum([y[i]**2 for i in range(len(y))])

# calculate the parameter estimates
n = len(x)
a = (sum_xy - (sum_x * sum_y) / n) / (sum_xx - (sum_x**2) / n)
b = (sum_y - a * sum_x) / n

# calculate the root-mean-square error
sum_of_squared_differences = sum_yy + a**2 * sum_xx + b**2 * n - 2*a*sum_xy - 2*b*sum_y + 2*a*b*sum_x
root_mean_square_error = sqrt(sum_of_squared_differences / n)

# print the results
print("a = ", a)
print("b = ", b)
print("Root Mean Square Error = ", root_mean_square_error)
