'''
Author: Akash Yadav 
        1710003
        Integrated M.Sc Physics 
        National Institute of Technology, Patna 
'''
import random as rnd
import matplotlib.pyplot as plt
import math
import numpy as np

Num_of_steps = 100
#this function will give us random walks performed, upon calling
def walker_modified(steps) :
    '''this is modified walker function and it returns squared position '''
    initial_pos = 0
    x= initial_pos
    step_size = 1
    
    x_avg_data=[]
    step_data = []
    for i in range(0,steps):
        x = x + (step_size*rnd.choice([1,-1]))**2
        x_avg_data.append(x)
        step_data.append(i+1)
    return x_avg_data,step_data


# for more than one walker (... say m walkers)
m = 5
sq_avg = np.zeros(Num_of_steps)
for i in range(0,m):
    Y,X = walker_modified(Num_of_steps)
    sq_avg = sq_avg + Y
    plt.scatter(X,Y) 

sq_avg = sq_avg/m
plt.plot(X,sq_avg)   
    #  plt.scatter(X,Y)
plt.title("Random walk problem in 1-D")
plt.xlabel("number of steps")
plt.ylabel("distance from origin")
plt.show() 





