import re

def valide_pass(part, first, second, criteria, password):
    if part == 1:
        result = sum(letter == criteria, for letter in password)
        return (first <= sum(result) <= second)
    else:
        return bool(password[first - 1] == criteria) != bool(password[second - 1] == criteria)
        
        
def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
    data = map(lambda x: re.match("([0-9]*)-([0-9]*) ([^:]+): ([^\n]+)", x).groups(), data)

    part = 2
    print(sum(test_password(part, *d) for d in data))


if __name__ == "__main__":
    main()