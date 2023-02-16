import numpy as np
import matplotlib.pyplot as plt

# function
def funcAdvec(x):
    y = np.zeros(len(x))
    for i in range(0, len(x)):
        if x[i] < 400 or x[i] > 600:
            y[i] = 0
        elif(x[i] < 500):
            y[i] = 0.1*(x[i] - 400)
        else:
            y[i] = 20 - 0.1*(x[i] - 400)
    return y

def linearInterp(a, y1, y2):
    return a*y1 + (1-a)*y2
def cubicInterp(a, x1, x2, x3, x4):
    return -a*(1-a**2)  *x1/6   \
        + a*(1+a)*(2-a) *x2/2   \
        + (1-a**2)*(2-a)*x3/2   \
        - a*(1-a)*(2-a) *x4/6

u = 0.75
dt = 1
dx = 50
x0 = np.arange(0, 1000, dx)
y0 = funcAdvec(x0)
xmax = max(x0)
sz = len(x0)
y1 = np.zeros(sz)
c = u*dt/dx
plt.plot(x0, y0, "+-")
for j in range(sz):
    xjd = x0[j] - u*dt
    # if xjd < 0:
    #     xjd = xjd + xmax
    m = int(np.floor(xjd/dx))
    # print(xjd, m, x0[m]) #m and m +1
    print(xjd, m) #m and m +1
    
plt.show()


