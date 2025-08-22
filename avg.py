# temperatures = [33.4,55.3,22.5,44.3,66.5]

# total = 0
# for temp in temperatures:
#     total+=temp

# average = total/len(temperatures)    

# print(average)


import numpy as np

temperatures = np.array([33.4,55.3,22.5,44.3,66.5])
average = np.mean(temperatures)
print(average)