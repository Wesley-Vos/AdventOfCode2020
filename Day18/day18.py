def calculate_line_part1(line):
    sum_val = line[0]
    for i in range(1, len(line)):
        if line[i] == "+":
            sum_val += line[i+1]
        elif line[i] == "*":
            sum_val *= line[i+1]
        i += 1

    return sum_val


def calculate_line_part2(line):
    i = 1
    while i < len(line):
        op = line[i]
        if op == "+":
            line[i] = line[i-1]+line[i+1]
            line.pop(i+1)
            line.pop(i-1)
            i -= 2
        i += 2

    sum_val = line[0]
    for i in range(1, len(line), 2):
        sum_val *= line[i+1]
    return sum_val


def calculate_line(line, part):
    if line[0] == "(":
        line = line[1:-1]
    line = [int(i) if i.isdigit() else i for i in line.split(" ")]
    if part == 1:
        return calculate_line_part1(line)
    elif part == 2:
        return calculate_line_part2(line)


def remove_parentheses(line, part):
    for i, ch in enumerate(line):
        if ch == "(":
            begin = i
        elif ch == ")":
            line = line[0:begin] + \
                str(calculate_line(line[begin:i+1], part)) + line[i+1:]
            return remove_parentheses(line, part)
    return line


def run(raw_data, part):
    data = []
    for raw_line in raw_data:
        line = remove_parentheses(raw_line, part)
        data.append(calculate_line(line, part))

    return(sum(data))


def main():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()

    print("Part 1:", run(raw_data, 1))
    print("Part 2:", run(raw_data, 2))


if __name__ == "__main__":
    main()
