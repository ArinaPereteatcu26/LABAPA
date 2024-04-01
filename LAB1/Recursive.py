import time
import matplotlib.pyplot as plt
from decimal import Decimal, Context, ROUND_HALF_EVEN


# Recursion
def fibonacci_recursive(n):
    if n <= 0:
        print("Ivalid input: n must be positive int")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Dynamic programming
def fibonacci_dynamic(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n]

# Arrays
def fibonacci_array(n):
    if n <= 0:
        return "Invalid"
    arr = [0, 1]
    if n > 2:
        for i in range(2, n):
            arr.append(data[i - 1] + arr[i - 2])
    return arr[n - 1]

#Itterative
def fibonacci_itterative(n):
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    return x

# Using power of the matrix
def fibonacci_matrix(n):
    FM = [[1, 1],
         [1, 0]]
    if n == 0:
        return 0
    power(FM, n - 1)
    return FM[0][0]

def multiply(F, M):
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    M = [[1, 1], [1, 0]]
    for i in range(2, n + 1):
        multiply(F, M)

#Binet formula
def fibonacci_binet(n):
    ctx = Context(prec=60, rounding=ROUND_HALF_EVEN)
    phi = Decimal((1 + Decimal(5**(1/2))))
    phi2 = Decimal((1 - Decimal(5**(1/2))))

    return int((ctx.power(phi, Decimal(n)) - ctx.power(phi2,Decimal(n))) / (2**n * Decimal(5**(1/2))))

# Function to measure execution time
def measure_time(func, arg):
    start_time = time.time()
    result = func(arg)
    end_time = time.time()
    return result, end_time - start_time

# Function to print results in a table
def print_results_table(method_name, input_series, times):
    print(f"{'n':<10} {'Time (seconds)':<20}")
    print("-" * 30)
    for n, time_taken in zip(input_series, times):
        print(f"{n:<10} {time_taken:<20.4f}")
    print("\n")

input_series_1 = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
input_series_2 = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

results = {method.__name__: {'values': [], 'times': []} for method in
           [fibonacci_recursive,
         fibonacci_dynamic, fibonacci_array, fibonacci_matrix, fibonacci_binet, fibonacci_itterative]}

for n in input_series_1:
    _, time_taken = measure_time(fibonacci_recursive, n)
    results['fibonacci_recursive']['times'].append(time_taken)

for n in input_series_2:
    for method in [fibonacci_dynamic, fibonacci_array, fibonacci_matrix, fibonacci_binet, fibonacci_itterative]:
        _, time_taken = measure_time(method, n)
        results[method.__name__]['times'].append(time_taken)

for method_name, data in results.items():
    print(f"Results for {method_name} method:")
    print_results_table(method_name, input_series_1 if method_name == 'fibonacci_recursive' else input_series_2, data['times'])

for method_name, data in results.items():
    plt.figure(figsize=(10, 6))
    if method_name == 'fibonacci_recursive':
        plt.plot(input_series_1, data['times'], marker='o', label=method_name, color='m')
        for n, time_taken in zip(input_series_1, data['times']):
            plt.text(n, time_taken, f'{time_taken:.4f} sec', ha='right', va='bottom', fontsize=8)
    else:
        plt.plot(input_series_2, data['times'], marker='o', label=method_name, color='m')
        for n, time_taken in zip(input_series_2, data['times']):
            plt.text(n, time_taken, f'{time_taken:.4f} sec', ha='right', va='bottom', fontsize=8)


    plt.title(f'Execution Time for {method_name} method')
    plt.xlabel('Fibonacci Nr')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.grid(True)

    # Adjust y-axis scale for better visualization
    max_time = max(data['times'])
    if max_time < 1:
        plt.ylim(0, 1)
    else:
        plt.ylim(0, max_time * 1.2)

    plt.show()