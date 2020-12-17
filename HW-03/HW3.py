import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from matplotlib import style


style.use('dark_background')

title = 'Signals and Systems (Fall 2020) - Amirhossein Alibakshi (9731096)\nHomework 3'

def fourier (T ,  x_t):
    start = 0
    end = T
    step = 0.001
    w=((np.pi)*2)/T
    a = []
    b = []
    t = np.arange(start, end, step)
    for i in range(0,12):
        x1 = x_t * np.sin(t*w*i)
        x2 = x_t * np.cos(t*w*i)
        integral_sin = np.sum(x1) * step
        integral_cos = np.sum(x2) * step
        # print(integral_sin)  # = 2
        # print(integral_cos)
        a.insert(i,(2 / T) * integral_cos)
        b.insert(i,2 / T * integral_sin)
    
    a_numpy = np.array(a)
    b_numpy = np.array(b)
    sum1 = a[0] / 2
    f, plots = plt.subplots(2,6)
    f2, plott = plt.subplots(1,1)   
    f2.suptitle(title)
    f.suptitle(title)
    color = ['red', 'blue', 'green', 'yellow', 'purple', 'violet', 'orange', 'cyan', 'white', 'brown' , 'pink']
    for k in range(0,12):
        sum1 +=  (a[k] * np.cos(k * ((np.pi * 2) / T) * t)) + (b[k] * np.sin(k * ((np.pi * 2) / T) * t))
        x = k // 6
        y = k % 6
        if k != 11:
            plt.plot(t, sum1, color=color[k % len(color)], label='k = {}'.format(k))
            plt.legend()
        plots[x][y].plot(t, sum1, color=color[k % len(color)])
        plots[x][y].set_title('k = {}'.format(k))
        # plt.plot(t, sum1)
    # plt.show()

n=np.arange(-3, 3, 0.001)
t=np.arange(-3, 3, 0.001)
choices=[1,-1]
conditions=[n<0 , n>=0]
X=np.select(conditions,choices)

plt.plot(n, X, 'r', label="X1")
plt.xlabel('t')
plt.ylabel('X')
plt.legend()
# plt.show()



conditions_2=[ (t > -3) & (t < -2) , (t > -2) & (t <= -1) , (t > -1) & (t <= 1) , (t > 1) & (t <= 2) , (t > 2) & (t <= 3) ]
choices_2=[0 ,t + 2 , -1 * t , t - 2 ,0]

X2=np.select(conditions_2, choices_2)
plt.plot(n, X2, 'y', label="X2")
plt.xlabel('t-axis')
plt.ylabel('X-axis')
plt.legend()
# plt.show()
fourier (6 ,  X2)
fourier (6 ,  X)
plt.show()
