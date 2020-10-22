# # # # # # # # # # # # # # # # # # # # #
#                                       #
#    Signals and Systems                #
#    Homework 1                         #
#    Question 1                         #
#    Amirhossein Alibakhshi (9731096)   #
#                                       #
# # # # # # # # # # # # # # # # # # # # #

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style

start = -3
stop = 3
step = 0.001
t = np.linspace(start, stop, int((stop - start)/step))
title = 'Signals and Systems (Fall 2020) - Amirhossein Alibakshi (9731096)\nHomework 1 / Question 1'

x1 = np.exp(-3 * t)
x2 = np.heaviside(t, 1)*x1
x3 = x2 + 2 * np.sin(t + 2)
def x4_function(t):
    if t > 1:
        result = np.heaviside(t, 1) * np.exp(-t) * (np.sin(t) + np.cos(t))
    elif -1 <= t <= 1:
        result = 1
    else:
        result = 0
    return result
x4 = [x4_function(i) for i in t]

style.use('dark_background')
f, plots = plt.subplots(4, sharex='col')
f.suptitle(title)

plots[0].plot(t, x1, color='red')
plots[0].set_title('x1(t)')
plots[1].plot(t, x2, color='yellow')
plots[1].set_title('x2(t)')
plots[2].plot(t, x3, color='green')
plots[2].set_title('x3(t)')
plots[3].plot(t, x4, color='blue')
plots[3].set_title('x4(t)')
plt.show()