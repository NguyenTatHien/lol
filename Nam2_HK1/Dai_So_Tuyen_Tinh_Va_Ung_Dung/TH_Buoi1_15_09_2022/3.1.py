import numpy as np
from numpy import *
vec1 = np.array([1., 3., 5.])
print(vec1 * 2)
print(vec1 * vec1)
print(vec1 /2)
print(vec1 + vec1)

vec2 = array([2., 4.])
print(vec1 + vec2)
vec3 = array([2., 4., 6.])
print(vec1 + vec3)
print(vec1 / vec3)
print(vec1 * vec3)
print(2* vec1 + 5* vec3)

print(vec3[2])
vec4 = np.linspace(0, 20, 5)
print(vec4)

vec5 = np.zeros(5)
print(vec5)

vec6 = np.ones(5)
print(vec6)

vec7 = np.empty(5)
print(vec7)

print(np.rand(5))

v = np.array([1., 3., 5.])
print(np.sum(v))

print(v.shape)

print(v.transpose())

v1 = v[:2]
print(v1)

v[0] = 5
print(v)

print(v1)

v1[:2] = [1., 2., 3.]
print(v1)

v1[:2] = [1., 2]
print(v)

v3 = 2 * v[:2] + v1 * 3
print(v3)

v1 = [4, 6]
print(v3)

print(v)

print(v + 10.0)

print(np.sqrt(v))

print(np.cos(v))

print(np.sin(v))

print(np.dot(v1, v3))

print(v1.dot(v3))

print(v3.dot(v1))