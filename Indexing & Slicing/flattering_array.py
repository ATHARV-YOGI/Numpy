# convertind multi-dimentional array to 1D-array

import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel()) #ravel returns -> view
print(arr_2d.flatten()) #flatten returns -> copy