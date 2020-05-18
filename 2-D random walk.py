'''
Author: Akash Yadav 
        1710003
        Integrated M.Sc Physics 
        National Institute of Technology, Patna 
'''

# lets simulate random walk in two dimensions for one random walker 

import random as rnd
import matplotlib.pyplot as plt 
import numpy as np
import math

# we need a random direction generator for this simulation,let's design that ...

def random_point(x,y):
    raw_random_variable = rnd.random() 
    # we need to map this variable to [0,1) ---->>> [0,2pi)
    random_angle = raw_random_variable*(2*math.pi)
    step_size = 1

    #next random point in two dimensions will be  ...
    x= x + math.cos(random_angle) *step_size
    y= y + math.sin(random_angle) *step_size

    return (x,y)


def path_generator(steps,x_0,y_0):
    #this funcions will give us random path taken by walker 
    x= x_0
    y= y_0
    x_data = np.zeros(steps+1) 
    y_data = np.zeros(steps+1)
    x_data[0],y_data[0]= x_0,y_0

    for i in range(1,steps+1):
        x,y = random_point(x,y)
        x_data[i]= x
        y_data[i]= y

    return  x_data,y_data


#  lets call path_generator(step,x_0,y_0)
x_0= 0
y_0 =0 
number_of_steps = 200
X,Y = path_generator(number_of_steps,x_0, y_0)
plt.plot(X,Y,color='blue')
plt.scatter(X,Y,color='black')
plt.scatter(x_0,y_0,linewidths=10,marker = '*',color='red')
plt.scatter(X[-1],Y[-1],linewidths=10 ,marker = '*',color='green',)

plt.title("Random walk in two-dimensions")
plt.xlabel("x- axis")
plt.ylabel("y- axis")


plt.show()
























