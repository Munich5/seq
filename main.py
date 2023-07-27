import math

def generate_fibonacci_sequence(n):
    """Generate the Fibonacci sequence up to the nth term."""
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)
    return fib_sequence

def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def bubble_sort(arr):
    """Perform bubble sort on the input array."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    """Perform selection sort on the input array."""
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    """Perform insertion sort on the input array."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    num_terms = 10
    fibonacci_sequence = generate_fibonacci_sequence(num_terms)
    print("Fibonacci Sequence (first 10 terms):", fibonacci_sequence)

    numbers_to_check = [2, 7, 12, 17, 23, 30]
    for num in numbers_to_check:
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")

    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted List:", unsorted_list)

    bubble_sort(unsorted_list.copy())
    print("Bubble Sort:", unsorted_list)

    selection_sort(unsorted_list.copy())
    print("Selection Sort:", unsorted_list)

    insertion_sort(unsorted_list.copy())
    print("Insertion Sort:", unsorted_list)
