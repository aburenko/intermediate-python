from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use("fivethirtyeight")


def create_data_set(hm, variance, step=2, correlation="off"):
    val = 1
    ys_new = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys_new.append(y)
        if correlation == "positive":
            val += step
        elif correlation == "negative":
            val -= step
    xs_new = [i for i in range(hm)]
    return np.array(xs_new, dtype=np.float64), np.array(ys_new, dtype=np.float64)


def best_fit_slope_and_intercept(xs, ys):
    calc_m = mean(xs) * mean(ys) - mean(xs * ys)
    calc_m /= mean(xs) * mean(xs) - mean(xs ** 2)

    calc_b = mean(ys) - calc_m * mean(xs)
    return calc_m, calc_b


def squared_error(ys_origin, ys_line):
    return sum((ys_line - ys_origin) ** 2)


def coefficient_of_determination(ys_origin, ys_line):
    y_mean_line = np.array([mean(ys_origin) for _ in ys_origin])
    squared_error_regression = squared_error(ys_origin, ys_line)
    squared_error_y_mean = squared_error(ys_origin, y_mean_line)
    return 1 - (squared_error_regression / squared_error_y_mean)


# simple data
# xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
# ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)

# random data
xs, ys = create_data_set(40, 20, 2, correlation="positive")


m, b = best_fit_slope_and_intercept(xs, ys)

print(m, b)

regression_line = np.array([(m * x) + b for x in xs])

predict_x = 8
predict_y = (m * predict_x) + b

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, color='g', s=50)
plt.plot(xs, regression_line)
plt.show()
