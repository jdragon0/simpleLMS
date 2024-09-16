"""
reference : https://en.wikipedia.org/wiki/Least_mean_squares_filter
reference : https://www.geocities.ws/ranjit_raphael/FXLMS.html
block diagram :
- LMS
x(n)─────────┬─────────┐
             V         V
          h_hat(n)   h(n)
        ↗    |         |
        |    V         V
 e(n)<─LMS<─ + <────── + <──── v(n)      

 - FxLMS
 x(n)───────┬─────────>P(z)────────────+─>e(n)
            |                          |   |  
            ├───────>W(z)───────>H(z)──┘   |
            |         ^                    |
            V         |                    |
           C(z)       |                    |
            └───────>LMS<──────────────────┘
Author: Jinyong kim
email : jy9886.kim@samsung.com / jdragon0@naver.com
copyright : MIT
©2024 
"""
import numpy as np

def LMS(input,output,learningRate=0.01,filterSize=2**7,error_history=False):
    mu = learningRate
    e_history = []
    h_h = np.zeros(filterSize)  # h hat
    x = np.zeros(filterSize)
    n_iter = min(len(input),len(output))
    for n in range(n_iter):
        x = np.append(input[n] , x[0:filterSize-1])
        y_h = np.sum(np.dot(h_h, x)) 
        d = output[n] 
        e = d - y_h  
        e_history.append(e)
        h_h = h_h + mu * e * x 
    if error_history:
        return h_h , e_history
    else:
        return h_h

def FxLMS(input,output,filter,learningRate=0.01,filterSize=2**7,error_history=False):
    mu = learningRate
    e_history = []
    x = np.zeros(filterSize)
    y = np.zeros(filterSize)
    xp = np.zeros(filterSize)
    w = np.zeros(filterSize)
    n_iter = min(len(input),len(output))
    for n in range(n_iter):
        x = np.append(input[n],x[0:filterSize-1])
        yn = np.sum(x*w)
        y = np.append(yn,y[0:filterSize-1])
        ypn = np.sum(y*filter)
        dn = output[n]
        en = dn - ypn
        xpn = np.sum(x*filter)
        xp = np.append(xpn,xp[0:filterSize-1])
        w = w+mu*en*xp
        e_history.append(en)
    if error_history:
        return w , e_history
    else:
        return w
