'''Напишите функцию min_max_dist, которая принимает на вход неограниченное число векторов через запятую. 
Гарантируется, что все векторы, которые передаются, одинаковой длины.
Функция возвращает минимальное и максимальное расстояние между векторами в виде кортежа.'''

import numpy as np

def min_max_dist(*vectors):
    
    if len(vectors) == 1:
        return("Not enough data!")
        
    if len(vectors) == 2:
        return((np.linalg.norm(vectors[0]-vectors[1])),(np.linalg.norm(vectors[0]-vectors[1])))
        
    min_dist = np.linalg.norm(vectors[1]-vectors[0])
    max_dist = np.linalg.norm(vectors[1]-vectors[0])
    
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            
            if min_dist > np.linalg.norm(vectors[i]-vectors[j]):
                min_dist = np.linalg.norm(vectors[i]-vectors[j])
            
            if max_dist < np.linalg.norm(vectors[i]-vectors[j]):
                max_dist = np.linalg.norm(vectors[i]-vectors[j])
                
    return(min_dist,max_dist)

vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])

print(min_max_dist(vec1, vec2, vec3))
# (5.196152422706632, 10.392304845413264)