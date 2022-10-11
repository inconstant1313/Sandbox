import numpy as np
'''print(np.uint8(-456))
print(np.finfo(np.float16))
arr = np.array([1,5,2,9,10], dtype=np.int8)
nd_arr = np.array([
               [[12], [45], [78]],
               [[34], [56], [13]],
               [[34], [56], [13]],
               [[12], [98], [76]]
               ], dtype=np.int16)
print(arr.ndim)
print(nd_arr.shape)'''
arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
print(step)
