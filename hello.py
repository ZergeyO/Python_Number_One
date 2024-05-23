import os
import numpy as np
import matplotlib.pyplot as plt

A = 512
def f(x):
    return -(A+47)*np.sin(np.sqrt(np.abs(x/2+(A+47))))-x*np.sin(np.sqrt(np.abs(x-(A+47))))

start = -512
end = 512
step = 0.1

x = np.arange(start, end, step)

y = f(x)

plt.plot(x, y,'r')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции y = f(x)')
plt.grid(False)
plt.show()

directory = 'results'
if not os.path.exists(directory):
    os.makedirs(directory)
file_path = os.path.join(directory, 'results.txt')
data = np.column_stack((x, y))
np.savetxt(file_path, data, fmt='%.3f',delimiter='    ', header='x\t\tf(x)')
