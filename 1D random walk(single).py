'''
Author: Akash Yadav 
        1710003
        Integrated M.Sc Physics 
        National Institute of Technology, Patna 
'''
import random as rnd
import matplotlib.pyplot as plt
import math

initial_pos = 0
x = 0
step_size = 1
steps = 1000
x_data=[]
step_data =[]
for i in range(0,steps):
    x = x + step_size*rnd.choice([1,-1])
    x_data.append(x)
    step_data.append(i+1)
    # plt.scatter(i,x)


plt.title("Random walk problem in 1-D")
plt.xlabel("number of steps")
plt.ylabel("distance from origin")
plt.plot(step_data,x_data)
plt.show()






