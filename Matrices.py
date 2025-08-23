import numpy as np

m = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)

print(m)

a = np.array([1, 2, 3, 4, 5], dtype=float)
print(a.shape)

m = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
print(m.shape)



b = np.array([[2, 3, 4, 5], [1, 2, 3, 4]])

c = np.array([[2, 2, 2, 2], [1, 1, 1, 1]])

print(b * c)

#Matrix multiplication

d = np.array([[1, 2, 3],
              [0, 1, 2]])

e = np.array([[ 1, 2],
              [ 0, 4],
              [-1, 0]])

f = np.dot(d, e)
print(f)


#Transposing and reshaping matrices in numpy

g = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(g)
h = g.T
print(h)


i = np.array([[1, 2, 3],
              [4, 5, 6]])

j = i.reshape((3, 2))
print(j)



k = np.array([[1, 2, 3], [4, 5, 6]])
l = k.flatten()
print(l)