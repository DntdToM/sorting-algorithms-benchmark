import sys
import time
from sort_utils import read_numbers

"""
Sorting Program with 4 Different Algorithms.
Allows user to choose algorithm to sort data from file.

Algorithms:
1. Heap Sort - Heap-based sorting
2. Merge Sort - Divide and conquer (iterative)
3. Quick Sort - Fast sorting (iterative)
4. NumPy Sort - Built-in NumPy sorting
5. Run All - Compare all algorithms
"""

# ============== HEAP SORT ==============
def heapify(arr, n, i):
    """
    Adjust heap at position i.
    
    Args:
        arr: Array to sort
        n: Heap size
        i: Position to heapify
    """
    while True:
        left = 2 * i + 1
        right = left + 1
        largest = i
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest == i:
            return
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def heapsort(arr):
    """
    Heap Sort algorithm.
    Time complexity: O(nlogn)
    
    Args:
        arr: Array to sort (in-place)
    """
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements from heap
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0)


# ============== MERGE SORT ==============
def mergesort(arr):
    """
    Merge Sort algorithm (iterative).
    Time complexity: O(n log n)
    
    Args:
        arr: Array to sort (in-place)
    """
    n = len(arr)

    if n < 2:
        return
    
    width = 1
    src = arr[:]

    while width < n:
        dst = []

        for left in range(0, n, 2 * width):
            mid = min(left + width, n)
            right = min(left + 2 * width, n)

            i, j = left, mid

            # Merge two halves
            while i < mid and j < right:
                if src[i] <= src[j]:
                    dst.append(src[i])
                    i += 1
                else:
                    dst.append(src[j])
                    j += 1

            while i < mid:
                dst.append(src[i])
                i += 1

            while j < right:
                dst.append(src[j])
                j += 1

        src = dst
        width *= 2

    arr[:] = src


# ============== QUICK SORT ==============
def quicksort(arr):
    """
    Quick Sort algorithm (iterative).
    Time complexity: O(n log n) average, O(n²) worst case
    
    Args:
        arr: Array to sort (in-place)
    """
    if len(arr) < 2:
        return
    stack = [(0, len(arr) - 1)]

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        i, j = left, right
        pivot = arr[(left + right) // 2]
        
        # Hoare Partition != Lomuto Partition
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        if left < j:
            stack.append((left, j))
        if i < right:
            stack.append((i, right))


# ============== NUMPY SORT ==============
def numpy_sort(arr):
    """
    Sort using NumPy library.
    Time complexity: O(n log n) - quicksort/mergesort hybrid
    
    Args:
        arr: Array to sort
        
    Returns:
        Sorted array or None if NumPy not available
    """
    try:
        import numpy as np
    except ImportError:
        print("Need numpy: pip install numpy")
        return None
    
    return np.sort(arr)


# ============== MAIN PROGRAM ==============
def run_single_sort(algo_choice, data, input_path):
    """
    Run selected sorting algorithm.
    
    Args:
        algo_choice: Algorithm choice (1-4)
        data: Data to sort (will be copied to avoid interference)
        input_path: Input file path
        
    Returns:
        Execution time in milliseconds
    """
    # IMPORTANT: For choosing Option 5, We create a copy to avoid interference between algorithms
    data_copy = data[:]
    
    algo_names = {
        1: "Heap Sort",
        2: "Merge Sort",
        3: "Quick Sort",
        4: "NumPy Sort"
    }
    
    t0 = time.time()
    
    if algo_choice == 1:
        heapsort(data_copy)
    elif algo_choice == 2:
        mergesort(data_copy)
    elif algo_choice == 3:
        quicksort(data_copy)
    elif algo_choice == 4:
        result = numpy_sort(data_copy)
        if result is None:
            return None
        data_copy = result
    
    t1 = time.time()
    elapsed_ms = (t1 - t0) * 1000
    
    print(f"{algo_names[algo_choice]:12} | Time: {elapsed_ms:8.2f} ms")
    
    return elapsed_ms


def run_all_algorithms(input_path):
    """
    Run all 4 algorithms and compare results.
    Each algorithm runs on a fresh copy of data to ensure fair timing.
    
    Args:
        input_path: Input file path
    """
    data, _ = read_numbers(input_path)
    
    print(f"\n{'='*60}")
    print(f"COMPARING ALL ALGORITHMS")
    print(f"{'='*60}")
    print(f"Input: {input_path}")
    print(f"Elements: {len(data)}")
    print(f"{'='*60}")
    
    results = {}
    
    for algo_id in range(1, 5):
        result = run_single_sort(algo_id, data, input_path)
        if result is not None:
            results[algo_id] = result
    
    print(f"{'='*60}")
    
    if results:
        fastest = min(results, key=results.get)
        algo_names = {1: "Heap Sort", 2: "Merge Sort", 3: "Quick Sort", 4: "NumPy Sort"}
        print(f"Fastest: {algo_names[fastest]} ({results[fastest]:.2f} ms)")
    
    print(f"{'='*60}\n")


def main():
    """
    Main function - display menu and handle selection.
    """
    print("\n" + "="*60)
    print("SORTING ALGORITHMS COMPARISON")
    print("="*60)
    print("\nChoose sorting algorithm:")
    print("  1. Heap Sort")
    print("  2. Merge Sort")
    print("  3. Quick Sort")
    print("  4. NumPy Sort")
    print("  5. Run All (Compare)")
    print("="*60)
    
    # Get user choice
    try:
        choice = int(input("\nEnter choice (1-5): "))
        if choice not in [1, 2, 3, 4, 5]:
            print("Invalid choice!")
            return
    except ValueError:
        print("Please enter a number!")
        return
    
    # Get file path
    if len(sys.argv) >= 2:
        input_path = sys.argv[1]
    else:
        input_path = input("Enter input file path: ").strip()
    
    if choice == 5:
        run_all_algorithms(input_path)
    else:
        data, _ = read_numbers(input_path)
        print(f"\n{'='*60}")
        print(f"Input: {input_path} | Elements: {len(data)}")
        print(f"{'='*60}")
        run_single_sort(choice, data, input_path)
        print(f"{'='*60}\n")


if __name__ == "__main__":
    main()