import math


def cnt_trees(data, slope_r, slope_c):
    counter = 0
    r, c = 0, 0
    c_max = len(data[0])
    while r < (len(data) - 1):
        r += slope_r
        c = (c + slope_c) % c_max
        counter += (data[r][c] == "#")
    return counter


def main():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    part_1 = cnt_trees(data, 1, 3)
    part_2 = math.prod(cnt_trees(data, dx, dy)
                       for dx, dy in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])

    print("Part 1:", part_1)
    print("Part 2:", part_2)


if __name__ == "__main__":
    main()
