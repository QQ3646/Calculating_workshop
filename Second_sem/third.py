import math


def f(x):
    return math.e ** (-1 * x ** 2)


def leftReq(f, a, b, eps):
    runge = 99
    n = 1
    In = 0
    I2n = 0
    while runge > eps:
        In = I2n
        n *= 2
        I2n = 0
        for i in range(n):
            len_a_b_n = abs(a - b) / n
            new_a = a + len_a_b_n * i
            new_b = a + len_a_b_n * (i + 1)
            I2n += len_a_b_n * f(new_a)
        runge = (1 / 3) * abs(I2n - In)
    print("Left req method: ", I2n, n)

def CentrReq(f, a, b, eps):
    runge = 99
    n = 1
    In = 0
    I2n = 0
    while runge > eps:
        In = I2n
        n *= 2
        I2n = 0
        for i in range(n):
            len_a_b_n = abs(a - b) / n
            new_a = a + len_a_b_n * i
            new_b = a + len_a_b_n * (i + 1)
            I2n += len_a_b_n * f((new_a + new_b) / 2)
        runge = (1 / 3) * abs(I2n - In)
    print("Central req method: ", I2n, n)

def Trap(f, a, b, eps):
    runge = 99
    n = 1
    In = 0
    I2n = 0
    while runge > eps:
        In = I2n
        n *= 2
        I2n = 0
        for i in range(n):
            len_a_b_n = abs(a - b) / n
            new_a = a + len_a_b_n * i
            new_b = a + len_a_b_n * (i + 1)
            new_fa = f(new_a)
            new_fb = f(new_b)
            I2n += (1 / 2) * len_a_b_n * (new_fa + new_fb)
        runge = (1 / 3) * abs(I2n - In)
    print("Left req method: ", I2n, n)

def Simp(f, a, b, eps):
    runge = 99
    n = 1
    In = 0
    I2n = 0
    while runge > eps:
        In = I2n
        n *= 2
        I2n = 0
        for i in range(n):
            len_a_b_n = abs(a - b) / n
            new_a = a + len_a_b_n * i
            new_b = a + len_a_b_n * (i + 1)
            new_fa = f(new_a)
            new_fb = f(new_b)
            I2n += (len_a_b_n / 6) * (new_fa + new_fb + 4 * f((new_a + new_b) / 2))
        runge = (1 / 15) * abs(I2n - In)
    print("Simp method: ", I2n, n)

a, b, eps = map(float, input().split())
leftReq(f, a, b, eps)
CentrReq(f, a, b, eps)
Trap(f, a, b, eps)
Simp(f, a, b, eps)