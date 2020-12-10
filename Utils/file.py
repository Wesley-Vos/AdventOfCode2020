def input_int(file_path):
    with open(file_path) as f:
         return list(map(int, f.read().splitlines()))

def input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()