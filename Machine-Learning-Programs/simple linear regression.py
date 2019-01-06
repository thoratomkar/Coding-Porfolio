# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 16:40:49 2018

@author: omkar
"""

import numpy as np
import matplotlib.pyplot as plt

def weights(x,y):
    
    n=np.size(x)
    mean_x,mean_y= np.mean(x),np.mean(y)
    
    num=np.sum(x*y - n*mean_x*mean_y)
    den=np.sum(x**2-n*mean_x**2)
    
    b1=num/den;
    b0=mean_y-b1*mean_x
    
    return (b0,b1)

def cost_function(x, y, b0, b1):
    size = len(x)
    total_error = 0.0
    for i in range(size):
        total_error += ((y[i] - (b1*x[i] + b0))**2)
    return total_error / size

def update_weights(x, y, b0, b1, learning_rate):
    weight_deriv = 0
    bias_deriv = 0
    size = len(x)

    for i in range(size):
        # Calculate partial derivatives
        # -2x(y - (mx + b))
        weight_deriv += -2*x[i] * (y[i] - (b1*x[i] + b0))

        # -2(y - (mx + b))
        bias_deriv += -2*(y[i] - (b1*x[i] + b0))

    # We subtract because the derivatives point in direction of steepest ascent
    b1 -= (weight_deriv / size) * learning_rate
    b0 -= (bias_deriv / size) * learning_rate

    return b0, b1

def train(x, y, b0, b1, learning_rate, iters):
    for i in range(iters):
        b0,b1 = update_weights(x, y, b0, b1, learning_rate)

    
    return (b0, b1)

def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show() 
  
def main(): 
    # observations 
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 
  
    # estimating coefficients 
    b = weights(x, y)
    b0=b[0]
    b1=b[1]
    b=train(x,y,b0,b1,0.0001,1000)
    print("Estimated coefficients:\nb_0 = {} \nb_1 = {}".format(b[0], b[1])) 
  
    # plotting regression line 
    plot_regression_line(x, y, b) 
    
if __name__ == "__main__": 
    main()