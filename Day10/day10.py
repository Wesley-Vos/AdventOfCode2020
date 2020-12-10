from collections import Counter, defaultdict


def find_differences(adapters):
    diff = Counter()
    for i, adapter in enumerate(adapters):
        if i != 0:
            diff[adapter - adapters[i-1]] += 1

    return diff[1]*diff[3]


def find_distinct_ways(i, adapters):
    ways = defaultdict(int)
    ways[0] = 1
    for i, adapter in enumerate(adapters):
        if i != 0:
            ways[adapter] = ways[adapter - 1] + \
                ways[adapter - 2] + ways[adapter - 3]
    return ways[adapters[-1]]


def main():
    with open("input.txt") as f:
        adapters = list(map(int, f.read().splitlines()))
    adapters += [0, max(adapters) + 3]
    adapters.sort()

    print("Part 1:", find_differences(adapters))
    print("Part 2:", find_distinct_ways(1, adapters.copy()))


if __name__ == "__main__":
    main()
