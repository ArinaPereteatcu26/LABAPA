import time
import matplotlib.pyplot as plt
import numpy as np
import random

#quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

#merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1     # left = 2i + 1
    right = 2*i + 2    # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

#radix_sort(arr)

def calculate_execution_time(sort_func, arr):
    start_time = time.time()
    sorted_arr = sort_func(arr)
    end_time = time.time()
    return end_time - start_time, sorted_arr

def plot_graph(execution_times, labels):
    x = np.arange(len(execution_times))
    plt.bar(x, execution_times, align='center', alpha=0.5)
    plt.xticks(x, labels)
    plt.ylabel('Execution Time (s)')
    plt.title('Sorting Algorithm Execution Times')
    plt.tight_layout()
    plt.show()

sizes = [1000, 2000, 3000, 4000, 5000]
sort_functions = [quick_sort, merge_sort, heap_sort, radix_sort]
sort_names = ['Quick Sort', 'Merge Sort', 'Heap Sort', 'Radix Sort']
execution_times = {name: [] for name in sort_names}

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

for size in sizes:
    arr = generate_random_array(size)
    for sort_func, name in zip(sort_functions, sort_names):
        time_taken, _ = calculate_execution_time(sort_func, arr.copy())
        execution_times[name].append(time_taken)

for name, times in execution_times.items():
    print(f"{name}: {times}")

for name, times in execution_times.items():
    plt.plot(sizes, times, label=name)

plt.xlabel('Array Size')
plt.ylabel('Execution Time (s)')
plt.title('Sorting Algorithm Execution Times')
plt.legend()
plt.show()

