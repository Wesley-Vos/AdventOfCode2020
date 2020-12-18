from collections import Counter, defaultdict
import re


def int_to_bin(val):
    return '{:036b}'.format(int(val))


def write_mem(address, val, mem):
    mem[address] = val


def write_masked_val(address, val, mask, mem):
    val_str = int_to_bin(val)
    for i, c in enumerate(val_str):
        if mask[i] in ("1", "0"):
            val_str = val_str[0:i] + mask[i] + val_str[(i+1):]

    write_mem(address, int(val_str, 2), mem)


def write_masked_mem(pos, address_str, val, mask, mem):
    print(pos, len(address_str), len(mask))
    if pos == len(address_str):
        write_mem(int(address_str, 2), int(val), mem)
        return

    if mask[pos] == "X":
        address_str1 = address_str[0:pos] + "0" + address_str[(pos+1):]
        address_str2 = address_str[0:pos] + "1" + address_str[(pos+1):]
        write_masked_mem(pos + 1, address_str1, mask, val, mem)
        write_masked_mem(pos + 1, address_str2, mask, val, mem)
    elif mask[pos] == "1":
        address_str = address_str[0:pos] + "1" + address_str[(pos+1):]
        write_masked_mem(pos + 1, address_str, mask, val, mem)
    elif mask[pos] == "0":
        write_masked_mem(pos + 1, address_str, mask, val, mem)


def run(program, part):
    mem = defaultdict(int)
    for op, address, val in program:
        if op == "mask":
            mask = val
        elif op[0:3] == "mem":
            if part == 1:
                write_masked_val(address, val, mask, mem)
            elif part == 2:
                write_masked_mem(0, int_to_bin(address), val, mask, mem)

    return sum([mem[i] for i in mem])


def main():
    with open("input.txt") as f:
        program = re.findall(r"(mask|mem\[([0-9]*)\]) = ([0-9X]*)", f.read())

    print("Part 1:", run(program, 1))
    print("Part 2:", run(program, 2))


if __name__ == "__main__":
    main()
