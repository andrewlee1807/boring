import numpy as np
import random
from numpy.linalg import norm as dist
# from scipy.spatial.distance import cdist as distance

# def grad(x):
#     return 2*x+ 5*np.cos(x)

# def cost(x):
#     return x**2 + 5*np.sin(x)

# def myGD1(eta, x0):
#     x = [x0]
#     for it in range(100):
#         x_new = x[-1] - eta*grad(x[-1])
#         if abs(grad(x_new)) < 1e-3:
#             break
#         x.append(x_new)
#     return (x, it)

square = lambda x: x**2

# def square(x):
#     return x*x

def difference_quotient(f, x, h):
    return (f(x+h) - f(x)) / h

def derivative(x):
    return 2*x


derivate_estimation = lambda x: difference_quotient(square, x, h = 0.00001)

import matplotlib.pyplot as plt
x = range(-10,10)

# plt.plot(x, list(map(derivative, x)), "rx", label="Actual")
# plt.plot(x, list(map(derivate_estimation, x)), "b+", label="Estimate")
# plt.legend()
# plt.show()


# partial derivatives 
def partial_difference_quotient(f, v, i, h):
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h
# approximating the gradient 
def estimate_gradient(f, v, h =0.00001):
    return [partial_difference_quotient(f,v,i,h) for i,_ in enumerate(v)]

# f = lambda v: v[0]**2 + v[0]*v[1] - 1
# v = [1,3]
# es = estimate_gradient(f,v)
# print(es)


def step(v, direction, step_size):
    return [v_i + step_size*direction_i for v_i, direction_i in zip(v, direction)]
def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

def distance(u,v):
    # print(np.asu-v)
    return dist(np.array(u) - np.array(v))

v = [random.randint(-10, 10) for i in range(3)]
tolerance = 0.0000001
print(v)
while True:
    gradient = sum_of_squares_gradient(v)
    next_v = step(v, gradient, -0.01)
    if distance(next_v, v) < tolerance:
        break
    v = next_v
    print(gradient)



def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    step_sizes = [100,10,1,0.1,0.01,0.001,0.0001,0.00001]
    theta = theta_0
    value = target_fn(theta)
    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size) for step_size in step_sizes]

        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        if abs(value - next_thetas) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value



# (x1, it1) = myGD1(.1, -5)
# (x2, it2) = myGD1(.1, 5)
# print(f"Solution x1 = {x1[-1]}, cost = {cost(x1[-1])}, obtained after {it1} iterations")
# print(f"Solution x2 = {x2[-1]}, cost = {cost(x2[-1])}, obtained after {it2} iterations")

