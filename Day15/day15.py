def find_x(data, x, i):
    cnt = 0
    for idx, d in enumerate(data):
        cnt += (d == x)
        if cnt == i:
            return idx + 1
    return -1


def main():
    data = [1, 0, 16, 5, 17, 4]
    test_data = [0, 3, 6]
    data = data

    history = {value: i + 1 for i, value in enumerate(data)}
    previous = list(history)[-1]

    for turn in range(len(history), 30_000_000):
        history[previous], previous = turn, turn - history.get(previous, turn)
    print(previous)


if __name__ == "__main__":
    main()
