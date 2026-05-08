import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


y_array = [0.742, 0.622, 0.537, 0.465]
x_array = [48, 242, 299, 484]
y_error = [0.011, 0.048, 0.112, 0.078]

plt.errorbar(x_array, y_array, yerr=y_error, marker='o', capsize=4, color='red')
plt.show()

slope, intercept = np.polyfit(x_array, y_array, 1, rcond=None, full=False, w=None, cov=False)
print(slope)
print(intercept)

y_array = [0.742, 0.622, 0.537, 0.465]
x_array = [48, 242, 299, 484]
y_error = [0.011, 0.048, 0.112, 0.078]

plt.errorbar(x_array, y_array, yerr=y_error, marker='o', capsize=4, color='red')
plt.show()


y_array = [0.757, 0.618, 0.627, 0.414]
x_array = [48, 242, 299, 484]
y_error = [0.021, 0.066, 0.057, 0.021]

slope, intercept = np.polyfit(x_array, y_array, 1, rcond=None, full=False, w=None, cov=False)
print(slope)
print(intercept)
