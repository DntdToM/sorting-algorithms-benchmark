# Sorting Algorithms Comparison

This project implements and compares 4 sorting algorithms on different datasets.

##  Quick Start

### 1. Generate Datasets (if not exist)
```bash
python dataset_creating.py
```
This creates 10 sequences in `datasets/` folder:
- `seq01_float_asc.txt` - Float ascending
- `seq02_float_desc.txt` - Float descending
- `seq03-05_float_rand.txt` - Float random (3 sequences)
- `seq06-10_int_rand.txt` - Integer random (5 sequences)

### 2. Run Sorting Menu
```bash
python sorting_menu.py datasets/seq06_int_rand.txt
```

Or run without file argument:
```bash
python sorting_menu.py
```
Then enter file path when prompted.

### 3. Choose Algorithm
- **1** - Heap Sort
- **2** - Merge Sort
- **3** - Quick Sort
- **4** - NumPy Sort
- **5** - Run All (Compare all algorithms)

## Example Results

### Test 1: Float Ascending (1M numbers)
```
Heap Sort    | Time:  5365.64 ms
Merge Sort   | Time:  3465.06 ms
Quick Sort   | Time:  1112.41 ms
NumPy Sort   | Time:   320.48 ms
Fastest: NumPy Sort (320.48 ms)
```

### Test 2: Float Random (1M numbers)
```
Heap Sort    | Time: 10596.69 ms
Merge Sort   | Time:  5803.43 ms
Quick Sort   | Time:  3436.43 ms
NumPy Sort   | Time:   358.55 ms
Fastest: NumPy Sort (358.55 ms)
```

## Notes

- **Option 5** creates a fresh copy of data for each algorithm to ensure fair timing
- All algorithms are iterative (not recursive) to avoid stack overflow
- Quick Sort uses Hoare partition scheme
- Dataset seed is fixed (42) for reproducibility

## Files

- `sorting_menu.py` - Main program with all 4 sorting algorithms
- `dataset_creating.py` - Dataset generator
- `sort_utils.py` - Utility functions for reading data
- `datasets/` - Generated datasets folder
