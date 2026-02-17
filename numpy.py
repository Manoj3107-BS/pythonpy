import numpy as np
arr=np.array([[[2,4,3],
[23,5,66],
[22,54,77]]])
a=np.sum(arr,axis=1)
b=np.argmax(a)
print(a)
print(b)
print(arr[b])