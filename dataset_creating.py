import random
import time
from pathlib import Path

"""
Simple dataset generator for sorting algorithms.
Creates 10 sequences (~1M numbers each):
  - Seq 1: Float ascending
  - Seq 2: Float descending  
  - Seq 3-5: Float random
  - Seq 6-10: Integer random
"""

# Configuration
N = 1_000_000 
OUTPUT_DIR = Path(__file__).parent / "datasets"
SEED = 42 

# Float range: 0.0 to 1,000,000.0
FLOAT_MIN, FLOAT_MAX = 0.0, 1_000_000.0

# Integer range: 0 to 1,000,000,000
INT_MIN, INT_MAX = 0, 1_000_000_000


def generate_float_random(n, seed_offset=0):
    """Generate n random floats."""
    rng = random.Random(SEED + seed_offset)
    return [rng.uniform(FLOAT_MIN, FLOAT_MAX) for _ in range(n)]


def generate_int_random(n, seed_offset=0):
    """Generate n random integers."""
    rng = random.Random(SEED + seed_offset)
    return [rng.randint(INT_MIN, INT_MAX) for _ in range(n)]


def save_to_file(data, filepath):
    """Save data to file, one number per line."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        for num in data:
            f.write(f"{num}\n")


def main():
    """Generate all 10 sequences."""
    print(f"\n{'='*60}")
    print(f"DATASET GENERATOR")
    print(f"{'='*60}")
    print(f"Generating {N:,} numbers per sequence...")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"{'='*60}\n")
    
    # Sequence 1: Float ascending
    print("1/10: Generating float ascending...")
    t0 = time.time()
    data = generate_float_random(N, seed_offset=1)
    data.sort()
    save_to_file(data, OUTPUT_DIR / "seq01_float_asc.txt")
    print(f"      Done in {time.time() - t0:.1f}s")
    
    # Sequence 2: Float descending
    print("2/10: Generating float descending...")
    t0 = time.time()
    data = generate_float_random(N, seed_offset=2)
    data.sort(reverse=True)
    save_to_file(data, OUTPUT_DIR / "seq02_float_desc.txt")
    print(f"      Done in {time.time() - t0:.1f}s")
    
    # Sequences 3-5: Float random
    for i in range(3, 6):
        print(f"{i}/10: Generating float random...")
        t0 = time.time()
        data = generate_float_random(N, seed_offset=i)
        save_to_file(data, OUTPUT_DIR / f"seq{i:02d}_float_rand.txt")
        print(f"      Done in {time.time() - t0:.1f}s")
    
    # Sequences 6-10: Integer random
    for i in range(6, 11):
        print(f"{i}/10: Generating integer random...")
        t0 = time.time()
        data = generate_int_random(N, seed_offset=i)
        save_to_file(data, OUTPUT_DIR / f"seq{i:02d}_int_rand.txt")
        print(f"      Done in {time.time() - t0:.1f}s")
    
    print(f"\n{'='*60}")
    print(f"All datasets generated successfully!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()