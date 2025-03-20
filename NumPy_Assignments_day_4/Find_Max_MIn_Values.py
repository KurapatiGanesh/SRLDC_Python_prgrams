import numpy as np
arr=np.random.randint(1,100,10)

max=np.max(arr)
maxindex=np.argmax(arr)
min=np.min(arr)
minindex=np.argmin(arr)
print(arr)
print(f"Max value of Array:{max} Max value Index of Array:{maxindex}")
print(f"Max value of Array:{min} Max value Index of Array:{minindex}")
