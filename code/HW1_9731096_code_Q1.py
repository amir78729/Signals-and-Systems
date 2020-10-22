# # # # # # # # # # # # # # # # # # # # #
#                                       #
#    Signals and Systems                #
#    Homework 1                         #
#    Question 2                         #
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
limit = 20
t = []
π = np.pi
title = 'Signals and Systems (Fall 2020) - Amirhossein Alibakshi (9731096)\nHomework 1 / Question 2'

for x in range(-limit,limit):
    t.append(x)

# step function
def u(n, n0, xn):
    if n >= n0:
        return xn
    else :
        return 0
    
style.use('dark_background')
f, plots = plt.subplots(3,3)
f.suptitle(title)

# x1[n] = u[n] - u[n-3] + u[n-5]
x1 = [u(n, 0 , 1) - u(n, 3 , 1) + u(n, 5 , 1) for n in range(-limit, limit)]

# x2[n] = 2cos(2kπn)
x2_1 = [2 * np.cos(2 * π * 1 * n ) for n in range(-limit, limit)] # k = 1   
x2_2 = [2 * np.cos(2 * π * 2 * n ) for n in range(-limit, limit)] # k = 2   
x2_3 = [2 * np.cos(2 * π * 3 * n ) for n in range(-limit, limit)] # k = 3 

# x3[n] = 2cos(2kn)
x3_1 = [2 * np.cos(2 * 1 * n ) for n in range(-limit, limit)] # k = 1
x3_2 = [2 * np.cos(2 * 2 * n ) for n in range(-limit, limit)] # k = 2
x3_3 = [2 * np.cos(2 * 3 * n ) for n in range(-limit, limit)] # k = 3

# adding to plots
plots[0,0].stem(t, x1)
plots[0,0].set_title('x1(t)')

plots[1,0].stem(t, x2_1 ,label='k = 1')
plots[1,0].set_title('x2_1(t)')
plots[1,1].stem(t, x2_2 ,label='k = 2')
plots[1,1].set_title('x2_2(t)')
plots[1,2].stem(t, x2_3 ,label='k = 3')
plots[1,2].set_title('x2_3(t)')

plots[2,0].stem(t, x3_1 ,label='k = 1')
plots[2,0].set_title('x3_1(t)')
plots[2,1].stem(t, x3_2 ,label='k = 2')
plots[2,1].set_title('x3_2(t)')
plots[2,2].stem(t, x3_3 ,label='k = 3')
plots[2,2].set_title('x3_3(t)')
plots.legend()

plt.show()