import numpy as np

arr1=np.array([12,3,56,67])
arr2=np.array([26,86,56,28])
vertical_stack=np.vstack((arr1,arr2))
horizontal_stack=np.hstack((arr1,arr2))
print("Original Array:" ,arr1,arr2)
print("Horizonatl Stack:",horizontal_stack)
print("vertical Stack",vertical_stack)