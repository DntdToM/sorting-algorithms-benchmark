import os


def get_dtype(path):
    name = os.path.basename(path).lower()
    if "float" in name:
        return "float"
    if "int" in name:
        return "int"
    raise ValueError("Ten file phai co 'float' hoac 'int'.")


def read_numbers(path):
    dtype = get_dtype(path)
    with open(path, "r", encoding="utf-8") as f:
        tokens = f.read().split()
    if dtype == "int":
        arr = [int(t) for t in tokens]
    else:
        arr = [float(t) for t in tokens]
    return arr, dtype