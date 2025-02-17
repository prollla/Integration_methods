import numpy
import matplotlib.pyplot as plt
import scipy.integrate as integrate


def method_monte_karlo(a, b, n):
    h = (b - a) / n
    answer = 0
    x = numpy.random.uniform(a, b, n)
    for i in range(n):
        answer += get_value_function_with_one_variable(x[i])
    return answer * h


def method_monte_karlo_for_two_variables(a, b, c, d, n, m):
    h = (b - a) / n
    h1 = (d - c) / m
    x = numpy.random.uniform(a, b, n)
    y = numpy.random.uniform(c, d, m)
    answer = 0
    for i in range(n):
        for j in range(m):
            answer += get_value_function_with_two_variable(x[i], y[j])
    return answer * h * h1


def method_rectangles(a, b, n):
    h = (b - a) / n
    answer = 0
    for i in range(n):
        answer += get_value_function_with_one_variable(a + i * h)
    return answer * h


def method_trapeziums(a, b, n):
    h = (b - a) / n
    answer = 0
    for i in range(1, n):
        answer += get_value_function_with_one_variable(a + i * h)
    answer *= 2
    answer += get_value_function_with_one_variable(a) + get_value_function_with_one_variable(b)
    return answer * h / 2


def method_simpson(a, b, n):
    step = (b - a) / n
    sum = get_value_function_with_one_variable(a) + get_value_function_with_one_variable(
        b) + 4 * get_value_function_with_one_variable(b - step)
    for i in numpy.arange(a, b - 2 * step, step * 2):
        sum += 2 * get_value_function_with_one_variable(i) + 4 * get_value_function_with_one_variable(i + step)
    return sum * step / 3


def method_parabolas(a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(0, n + 1):
        if i == 0 or i == n:
            res += 7 * get_value_function_with_one_variable(a)
        if i % 2 != 0 and i % 3 != 0:
            res += 3 * get_value_function_with_one_variable(a)
        if i % 2 == 0 and i % 3 != 0:
            res += 3 * get_value_function_with_one_variable(a)
        if i % 3 == 0:
            res += 2 * get_value_function_with_one_variable(a)
        a += h
    res *= (3 * h) / 8
    return res


def method_bool(a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(0, n + 1):
        if i == 0 or i == n:
            res += 7 * get_value_function_with_one_variable(a)
        if i % 2 != 0:
            res += 32 * get_value_function_with_one_variable(a)
        if i % 2 == 0 and i % 4 != 0:
            res += 12 * get_value_function_with_one_variable(a)
        if i % 4 == 0:
            res += 14 * get_value_function_with_one_variable(a)
        a += h
    return res * (2 * h) / 45


def method_gauss(a, b, n, count_node):
    answer = 0
    for i in range(n):
        answer += __calculate_sum(a + i * (b - a) / n, a + (i + 1) * (b - a) / n, count_node)
    return answer


def __calculate_sum(a, b, count_node):
    table_x = [
        [0], [-0.5773503, 0.5773503], [-0.7745967, 0, 0.7745967], [-0.8611363, -0.3399810, 0.3399810, 0.8611363],
        [-0.9061798, -0.5384693, 0, 0.5384693, 0.9061798],
        [-0.9324700, -0.6612094, -0.2386142, 0.2386142, 0.6612094, 0.9324700]
    ]
    table_c = [
        [2], [1, 1], [0.5555556, 0.8888889, 0.5555556], [0.3478548, 0.6521451, 0.6521451, 0.3478548],
        [0.4786287, 0.2369269, 0.5688888, 0.2369269, 0.4786287],
        [0.1713245, 0.3607616, 0.4679140, 0.4679140, 0.3607616, 0.1713245]
    ]

    h = (b - a) / 2
    x = (a + b) / 2
    sum = 0
    for i in range(count_node):
        xi = x + table_x[count_node - 1][i] * h
        sum += get_value_function_with_one_variable(xi) * table_c[count_node - 1][i]
    return sum * h


def main():
    print("Enter a: ", end='')
    a = float(input())
    print("Enter b: ", end='')
    b = float(input())
    print("Enter n: ", end='')
    n = int(input())

    print("Enter the count node for method Gauss: ", end='')
    count = int(input())

    print("===FUNCTION WITH ONE VARIABLES===")
    print(f"Method rectangles: {method_rectangles(a, b, n)}")
    print(f"Method trapezoidal: {method_trapeziums(a, b, n)}")
    print(f"Method parabolas: {method_simpson(a, b, n)}")
    print(f"Method cubic parabolas: {method_parabolas(a, b, n)}")
    print(f"Method Boole: {method_bool(a, b, n)}")
    print(f"Method Gauss: {method_gauss(a, b, n, count)}")
    print(f"Method Monte-Karlo: {method_monte_karlo(a, b, n)}")
    print("===FUNCTION WITH TWO VARIABLES===")
    print("Enter c: ", end='')
    c = float(input())
    print("Enter d: ", end='')
    d = float(input())
    print("Enter m: ", end='')
    m = int(input())
    print(f"Method Monte-Karlo: {method_monte_karlo_for_two_variables(a, b, c, d, n, m)}")

    get_graphic(a, b, n)


def get_value_function_with_one_variable(x):
    return numpy.e ** x


def get_value_function_with_two_variable(x, y):
    return (x ** 2) * numpy.sin(x) ** 3 + numpy.log(y)


def get_graphic(a, b, n):
    h = numpy.arange(1, n)
    z = integrate.quad(lambda x: get_value_function_with_one_variable(x), a, b)

    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    for i in h:
        y1.append(method_rectangles(a, b, i))
        y2.append(method_trapeziums(a, b, i))
        y3.append(method_simpson(a, b, i))
        y4.append(method_parabolas(a, b, i))
        y5.append(method_bool(a, b, i))
        y6.append(z[0])

    plt.title("Graphics")
    plt.xlabel("n")
    plt.ylabel("y1, y2, y3, y4, y5, y6")
    plt.grid()

    plt.plot(h, y1, label="Method rectangles")
    plt.plot(h, y2, label="Method trapezoidal")
    plt.plot(h, y3, label="Method parabolas")
    plt.plot(h, y4, label="Method cubic parabolas")
    plt.plot(h, y5, label="Method Boole")
    plt.plot(h, y6, label="Ideal")

    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()
