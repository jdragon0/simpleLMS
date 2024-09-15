"""
reference : https://en.wikipedia.org/wiki/Least_mean_squares_filter
block diagram :
x(n)───────┬─────────┐
           V         V
        h_hat(n)   h(n)
        ↗  |         |
        |  V         V
 e(n)<──── + <────── + <──── v(n)      

Author: Jinyong kim
email : jy9886.kim@samsung.com / jdragon0@naver.com
copyright : MIT
©2024 
"""
import numpy as np

def LMS(data,filteredData,learningRate=0.01,filterSize=2**7):
    mu = learningRate
    e_history = []
    h_h = np.zeros(filterSize)  # h hat
    n_iter = min(len(data),len(filteredData))
    for n in range(filterSize,n_iter):
        x = np.flip(data[n-filterSize:n]) 
        y_h = np.dot(h_h, x) 
        d = filteredData[n] 
        e = d - y_h  
        e_history.append(e)
        h_h = h_h + mu * e * x 
    return h_h , e_history

def LMS(data,filteredData,learningRate=0.01,filterSize=2**7):
    mu = learningRate
    e_history = []
    h_h = np.zeros(filterSize)  # h hat
    n_iter = min(len(data),len(filteredData))
    for n in range(filterSize,n_iter):
        x = np.flip(data[n-filterSize:n]) 
        y_h = np.dot(h_h, x) 
        d = filteredData[n] 
        e = d - y_h  
        e_history.append(e)
        h_h = h_h + mu * e * x 
    return h_h
