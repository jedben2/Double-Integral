import numpy as np
from tqdm import tqdm

# Set up x, y range
dx = 0.001
dy = 0.001
a, b = 0, 4
c, d = 1, 4

xs = np.linspace(a, b, int(np.abs(b - a) // dx))
ys = np.linspace(c, d, int(np.abs(d - c) // dx))
def f(x, y):
    #return 0.25 * (y ** 2 - x ** 2)
    #return np.exp(x * y)
    #return x * y
    return y * np.sin(x * y)

def inRegion(x, y):
    try:
        #if x + y >= 0 and x + y <= 4 and x <= y and y <= 3 * x: return True
        #if 0.5 * x <= y  and y <= x and 1 <= x * y and x * y <= 2: return True
        #if 0 <= x and x <= 2 and 0 <= y and y <= 1: return True
        if 1 <= y and y <= 4 and 1 <= x * y and x * y <= 4: return True
    except: pass
    return False

def double_integral():
    total = 0
    for x in tqdm(xs):
        for y in ys:
            if inRegion(x, y):
                total += f(x, y) * dx * dy
    return total

print(double_integral())