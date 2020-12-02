import itertools
import math

input_file = open("input.txt", "r")
input_data = []
for line in input_file.readlines():
    input_data.append(int(line.strip()))
input_file.close()


def find_sums(n):
    for combination in itertools.combinations(input_data, n):
        if sum(list(combination)) == 2020:
            print(math.prod(list(combination)))


find_sums(2)
find_sums(3)