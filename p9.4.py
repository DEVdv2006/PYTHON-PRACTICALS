import matplotlib.pyplot as plt  
import numpy as np   
x_values=np.linspace(-5,5,100)
y_values=np.maximum(0,x_values)
plt.plot(x_values,y_values,label='ReLU Function')
plt.axhline(0,color='black',linewidth=0.5)
plt.axvline(0,color='black',linewidth=0.5)
plt.title('ReLU Function')
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.legend()
plt.grid(True)
plt.show()