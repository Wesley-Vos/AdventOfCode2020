def count_trees(data, slope_r, slope_c):
    counter = 0
    r = 0
    c = 0
    cm = len(data[0])
    while r < (len(data) - 1):
        r += slope_r
        c = (c + slope_c) % cm
        counter += (data[r][c] == "#")
    return counter


def main():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    part_1 = count_trees(data, 1, 3)
    part_2 = count_trees(data, 1, 1) * part_1 * count_trees(data,
                                                            1, 5)*count_trees(data, 1, 7)*count_trees(data, 2, 1)

    print("Part 1:", part_1)
    print("Part 2:", part_2)


if __name__ == "__main__":
    main()
