import re


def valid_pass(part, first, second, criteria, password):
    if part == 1:
        result = sum(letter == criteria for letter in password)
        return (int(first) <= result <= int(second))
    else:
        return bool(password[int(first) - 1] == criteria) != bool(password[int(second) - 1] == criteria)


def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
    data = list(map(lambda x: re.match(
        "([0-9]*)-([0-9]*) ([^:]+): ([^\n]+)", x).groups(), data))

    print("Part 1:", sum(valid_pass(1, *d) for d in data))
    print("Part 2:", sum(valid_pass(2, *d) for d in data))


if __name__ == "__main__":
    main()
