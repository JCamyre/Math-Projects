import matplotlib.pyplot as plt 
import numpy as np 
from scipy.integrate import quad
  
# Creating vectors X and Y 
x = np.linspace(-2, 2, 1000) # x = -2 to x = 2, 1000 points/lines, the more points the smoother
y = x ** 3
  
fig = plt.figure(figsize = (10, 5)) 
# Create the plot 
plt.plot(x, y) 
  
# Show the plot 
plt.show() 

def function(x):
	return x ** 2

ans, err = quad(function, 0, 1)
print(ans)