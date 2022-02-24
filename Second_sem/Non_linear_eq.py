from input_engine import Function, input_function

f, eps = input_function()

# Bisection method (метод деления отрезка пополам (бисекций))

def bisect(f: Function, a: float, b: float, eps: float) -> (int, float):
    if f(a) * f(b) > 0:
        print(f"Некорректный интервал: у функции на [{a}, {b}] нет корней.")
        return
    iteration_counter = 0
    while abs(b - a) > eps:
        mid = (b + a) / 2
        if f(mid) * f(a) <= 0:
            b = mid
        else:
            a = mid
        iteration_counter += 1
    return iteration_counter, (b + a) / 2

res = bisect(f, -100, 100, eps)
print(f"Количество итераций: {res[0]}\nРезультат: {res[1]}")
# Fixed-point iteration (метод простой итерации)

def FPIteration():


# Successive over-relaxation (метод релаксации)

# Newton's method (метод Ньютона)
