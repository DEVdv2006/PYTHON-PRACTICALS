import matplotlib .pyplot as plt  
import random
marks=[random.uniform(0,10) for _ in range(100)]
plt.hist(marks,bins=10,range=(0,10),edgecolor='black')
plt.xlabel('Marks')
plt.ylabel('number of students')
plt.title('histogram of student marks')
plt.show()