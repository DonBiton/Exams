import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Определение функций
def f1(x):
    return x**3 - x  # y1 = x^3 - x

def f2(x):
    return 2*x - 1  # y2 = 2x - 1

# Разница функций для нахождения пересечений
def diff(x):
    return f1(x) - f2(x)

# Нахождение точек пересечения
x_roots = fsolve(diff, [-2, 0, 2])  # Три предположительных корня
y_roots = f1(x_roots)

# Построение графиков
x = np.linspace(-3, 3, 400)
y1 = f1(x)
y2 = f2(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$y_1 = x^3 - x$', color='blue')
plt.plot(x, y2, label=r'$y_2 = 2x - 1$', color='red')

# Отметим точки пересечения
plt.scatter(x_roots, y_roots, color='green', zorder=5)
for i in range(len(x_roots)):
    plt.text(x_roots[i], y_roots[i], f'({x_roots[i]:.2f}, {y_roots[i]:.2f})', color='green')

# Настройки графика
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.title("Графики функций $y_1 = x^3 - x$ и $y_2 = 2x - 1$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
