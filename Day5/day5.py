def main():
    with open("input.txt", "r") as f:
        data = f.read().split("\n")

    seat_ids = [int(row.replace("L", "0").replace("R", "1").replace("F", "0").replace("B", "1"), 2) for row in data]
    print("Part 1:", max(seat_ids))

    for seat_id in range(0, max(seat_ids)+1):
        if seat_id not in seat_ids and (seat_id - 1) in seat_ids and (seat_id + 1) in seat_ids:
            print("Part 2:", seat_id)
            break

if __name__ == "__main__":
    main()