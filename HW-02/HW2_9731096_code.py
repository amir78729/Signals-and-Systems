# # # # # # # # # # # # # # # # # # # # #
#                                       #
#    Signals and Systems                #
#    Homework 2                         #
#    Question 1                         #
#    Amirhossein Alibakhshi (9731096)   #
#                                       #
# # # # # # # # # # # # # # # # # # # # #

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style
import math

# convolution 
def convolve(input_1, input_2):
    input_1_length = len(input_1)
    input_2_length = len(input_2)
    result_length = input_1_length + input_2_length - 1
    result = np.zeros(result_length)
    input_1 =np.pad(input_1,(0, result_length - input_1_length),'constant')
    input_2 =np.pad(input_2,(0, result_length - input_2_length),'constant')
    #convolution sum formula ( Σ x[k].h[n - k] )
    for n in range (result_length):
        for k in range (result_length):
            if n >= k:
                result[n] = result[n] + input_2[n - k] * input_1[k]
    return result

# step function
def u(n, n0, xn):
    if n >= n0:
        return xn
    else :
        return 0

title = 'Signals and Systems (Fall 2020) - Amirhossein Alibakshi (9731096)\nHomework 2 / Question 1'    
t1 = np.arange(-10.0, 10.0, .1)
t1_convolve = np.arange(-20.0, 19.9, .1)

######

style.use('dark_background')
f, plots = plt.subplots(3, 1)
f.suptitle(title + ' (a)')
# x1(t) = 1/2(e^(-2t))u(t)
x1 = [.5 * math.exp(-2 * t) * u(t, 0 , 1) for t in t1]
# h1(t) = u(t) - u(t-5)
h1 = [u(t, 0 , 1) - u(t, 5 , 1) for t in t1]
y1 = convolve(x1, h1)
plots[0].stem(t1, x1)
plots[0].set_title('x1(t)')
plots[1].stem(t1, h1)
plots[1].set_title('h1(t)')
plots[2].stem(t1_convolve, y1)
plots[2].set_title('y1(t)')

######

t2 = np.arange(-5, 10, 1)
t2_convolve = np.arange(-10, 19, 1)
style.use('dark_background')
f, plots = plt.subplots(3, 1)
f.suptitle(title + ' (b)')
# x2[n] = (1/3)^-n*u[-n-1]
x2 = [(1 / 3)**(-n) * u(-n, 1 , 1) for n in t2]
# h2[n] = u[n-1]
h2 = [ u(n, 1 , 1) for n in t2]
y2 = convolve(x2, h2)
plots[0].stem(t2, x2)
plots[0].set_title('x2(t)')
plots[1].stem(t2, h2)
plots[1].set_title('h2(t)')
plots[2].stem(t2_convolve, y2)
plots[2].set_title('y2(t)')

######

t3 = np.arange(-5, 10, 1)
t3_convolve = np.arange(-10, 19, 1)
style.use('dark_background')
f, plots = plt.subplots(3, 1)
f.suptitle(title + ' (c)')
# x3[n] = u[n] - u[n-3] + u[n-5] - u[n-8] 
x3 = [ u(n, 0 , 1) -  u(n, 3 , 1) +  u(n, 5 , 1) -  u(n, 8 , 1)  for n in t3]
# h3[n] = u[n-1]
h3 = [ (1/3)**(n) * u(n, 0 , 1) for n in t3]
y3 = convolve(x3, h3)
plots[0].stem(t3, x3)
plots[0].set_title('x3(t)')
plots[1].stem(t3, h3)
plots[1].set_title('h3(t)')
plots[2].stem(t3_convolve, y3)
plots[2].set_title('y3(t)')

plt.show()