import numpy as np

a = np.array([1, 2, 3, 4, 5], dtype=float)
print(a + 2)
print(a - 1)

# λ∗ a ∈ Ra

a = np.array([1, 2, 3, 4, 5], dtype=float)

print(a)

b = 5*a

print(b)
print(a.size) 

c = np.array([1, 2, 3])
d = np.array([4, 5, 6])
print(c + d)
print(c - d)

# x⋅y=x1 y1 +x2 y2 +x3 y3

e = np.array([1, 2, 3])
f = np.array([4, 5, 6])
print(np.dot(e, f))
print(e / f)