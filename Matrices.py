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

# Matrix multiplication

d = np.array([[1, 2, 3], [0, 1, 2]])

e = np.array([[1, 2], [0, 4], [-1, 0]])

f = np.dot(d, e)
print(f)


# Transposing and reshaping matrices in numpy

g = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(g)
h = g.T
print(h)


i = np.array([[1, 2, 3], [4, 5, 6]])

j = i.reshape((3, 2))
print(j)


k = np.array([[1, 2, 3], [4, 5, 6]])
l = k.flatten()
print(l)

# Unit matrix

# ImA = AIn = A

m = np.eye(4, k=-1, dtype=float)
print(m)


# Inverse matrix

# AA^-1 = A^-1A = I

n = np.array([[1, 0, 3], [-1, -1, 2], [4, 7, 2]])

n_inv = np.linalg.inv(n)
print(n_inv)


# A+B=B+A
# AB!=BA
# A+(B+C)=(A+B)+C
# A(BC)=(AB)C
# A(B+C)=AB+AC
# (A+B)^T=A^T+B^T
# (AB)^T=B^T A^T
# (λA)^T=λA^T
# (A^T)^T=A
# (A^−1)^−1=A
# (AB)^−1=B^−1 A^−1
# I^−1=I


#np.ones((5,), dtype=float)
#np.ones((2, 3), dtype=int)

#np.zeros(5, dtype=float)
#np.zeros((2, 3), dtype=int)

#np.arange(5)
#np.arange(1, 3, 0.5)

#np.linspace(1, 5, num=5)
#np.linspace(1, 3, num=3)

#np.random.random(3)
#np.random.random((3, 3))

o = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(o[1, 1])
print(o[1:, 1])
print(o[0, :2])

p = np.zeros((3, 3), dtype="u4")
print(p)

q = np.array([u"\u2211", u"\u220F"], dtype="U")
print(q) # ['∑' '∏']

r = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(r.min())
print(r.max())
print(r.sum())
print(r.mean())
print(r.prod())