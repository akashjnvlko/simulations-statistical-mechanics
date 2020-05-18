# lets calculate value of pi using monte - carlo simulation 

import random 
import math
import matplotlib.pyplot as plt 
n = 2000
hits = 0 

for i in range(0,n):
    x = random.randint(-10000,10000)
    x= x/10000
    y = random.randint(-10000,10000)
    y= y/10000
    print(x,y)
    plt.plot(x,y,color= 'red')

    if math.sqrt(x**2 + y**2) <= 1 :
        hits = hits + 1 
        plt.scatter(x,y, color= 'red')
    else :
        plt.scatter(x,y, color= 'blue')



    
prob = hits/n
pi = 4 * prob 
print("value of pi = " ,pi)

plt.show()

