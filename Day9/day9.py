import itertools
import timeit


def find_invalid_number(preamble: list, n: int) -> int:
    for i in range(n, len(preamble)):
        number = preamble[i]
        combinations = list(itertools.combinations(preamble[(i-n):i], 2))
        sums = [sum(combination) for combination in combinations]
        if number not in sums:
            return number
    return -1


def find_contiguous_set(preamble: list, invalid_number: int) -> int:
    for start in range(0, len(preamble) - 1):
        end = start
        set_sum = 0
        while set_sum < invalid_number:
            set_sum += preamble[end]
            end += 1

        if set_sum == invalid_number and (end - start) >= 2:
            return min(preamble[start:end]) + max(preamble[start:end])
    return -1


def main():
    with open("input.txt") as f:
        preamble = list(map(int, f.read().splitlines()))

    invalid_number = find_invalid_number(preamble, 25)
    print("Part 1:", invalid_number)
    part2 = find_contiguous_set(preamble, invalid_number)
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
