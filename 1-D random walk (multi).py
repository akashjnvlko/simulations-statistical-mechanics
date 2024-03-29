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
def walker(steps) :

    initial_pos = 0
    x= initial_pos
    step_size = 1
    
    x_data=[]
    step_data = []
    for i in range(0,steps):
        x = x + (step_size*rnd.choice([1,-1]))
        x_data.append(x)
        step_data.append(i+1)
    return x_data,step_data


# for more than one walker (... say m walkers)
m = 20
avg = np.zeros(Num_of_steps)
sq_avg = np.zeros(Num_of_steps)
for i in range(0,m):
     Y,X = walker(Num_of_steps)
     avg = avg + Y
     plt.plot(X,Y) 

avg = avg/m
plt.plot(X,avg)   
    #  plt.scatter(X,Y)
plt.title("Random walk problem in 1-D")
plt.xlabel("number of steps")
plt.ylabel("distance from origin")
plt.show()
 





