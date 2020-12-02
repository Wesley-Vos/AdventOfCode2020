import itertools
import math

input_file = open("input.txt", "r")
input_data = list(map(lambda x: int(x), input_file.read().splitlines()))
input_file.close()

def find_sums(n):
    for combination in itertools.combinations(input_data, n):
        if sum(combination) == 2020:
            print(math.prod(combination))

find_sums(2)
find_sums(3)