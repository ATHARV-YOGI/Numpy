import numpy as np

arr_2d = np.array([[1,2],[9,10]])

new_arr_2d = np.insert(arr_2d,0,[54,56],axis=0)
print(new_arr_2d)