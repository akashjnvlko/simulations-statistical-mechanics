
import random as rnd
import matplotlib.pyplot as plt
import math


#this function will give us random walks performed, upon calling
def walker() :

    initial_pos = 0
    x= initial_pos
    step_size = 1
    steps = 200
    x_data=[]
    step_data = []
    for i in range(0,steps):
        x = x + (step_size*rnd.choice([1,-1]))
        x_data.append(x)
        step_data.append(i+1)
    return x_data,step_data


# for more than one walker (... say m walkers)
m = 5  

for i in range(0,m):
     Y,X = walker()
     plt.plot(X,Y)
    #  plt.scatter(X,Y)
plt.title("Random walk problem in 1-D")
plt.xlabel("number of steps")
plt.ylabel("distance from origin")
plt.show() 


