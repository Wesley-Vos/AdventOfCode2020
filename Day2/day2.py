import re


def valid_pass(part, first, second, criteria, password):
    if part == 1:
        result = sum(letter == criteria for letter in password)
        return (int(first) <= result <= int(second))
    elif part == 2:
        return (password[int(first) - 1] == criteria) ^ (password[int(second) - 1] == criteria)


def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
    pattern = "([0-9]*)-([0-9]*) ([^:]+): ([^\n]+)"
    data = list(map(lambda in_str: re.match(pattern, in_str).groups(), data))

    part_1 = sum(valid_pass(1, *d) for d in data)
    part_2 = sum(valid_pass(2, *d) for d in data)

    print("Part 1:", part_1)
    print("Part 2:", part_2)


if __name__ == "__main__":
    main()
