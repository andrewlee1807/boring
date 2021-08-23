import numpy as np
xs = np.asarray([45, 67, 32, 52, 94, 67, 32])
ys = np.asarray([67, 32])

def array_match(a, b):
    result = []
    for i in range(0, len(a)-len(b)+1):
        if (a[i:i+len(b)] == b).all():
            result.append(i)
    return None

a = ''.join(str(i) for i in xs)
b = ''.join(str(i) for i in ys)
print(a.index(b))

print(array_match(xs, ys))

