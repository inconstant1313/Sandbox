import numpy as np
a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])

l_a = np.linalg.norm(a)
l_b = np.linalg.norm(b)
l_c = np.linalg.norm(c)

l_sum_a_b = np.linalg.norm(a+b)
l_sum_b_c = np.linalg.norm(b+c)
l_sum_a_c = np.linalg.norm(a+c)
print(l_sum_a_b == (l_a+l_b), l_sum_b_c == (l_b+l_c), l_sum_a_c == (l_a+l_c))

distance_a_b = np.linalg.norm(a-b)
distance_b_c = np.linalg.norm(b-c)
distance_a_c = np.linalg.norm(a-c)
print(distance_a_b>100, distance_b_c>100, distance_a_c>100)

print(np.dot(a,b),np.dot(b,c),np.dot(a,c))

