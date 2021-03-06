import re


class PassportScanner:
    def __init__(self, file_path):
        self.passports = self._scan(file_path)

    def _scan(self, file_path):
        with open(file_path, "r") as f:
            raw_data = f.read().split("\n\n")

        scanned_passports = [Passport(line) for line in raw_data]
        return scanned_passports

    def count_passports(self):
        return sum((passport.present for passport in self.passports))

    def count_validated_passports(self):
        return sum((passport.validated for passport in self.passports))


class Passport:
    def __init__(self, raw_data):
        self.fields = self._parse_raw_data(raw_data)
        self.present = self._check_passport()
        self.validated = self._validate_passport()

    def _parse_raw_data(self, raw_data):
        pattern = r"(byr|eyr|iyr|hgt|hcl|ecl|pid|cid):([\S]*)"
        fields_parsed = re.findall(pattern, raw_data)
        fields = {key: value for key, value in fields_parsed}
        return fields

    def _check_passport(self):
        return len(self.fields) == 8 or (len(self.fields) == 7 and "cid" not in self.fields)

    def _validate_passport(self):
        if not self.present:
            return False
        byr = (1920 <= int(self.fields["byr"]) <= 2002)
        iyr = (2010 <= int(self.fields["iyr"]) <= 2020)
        eyr = (2020 <= int(self.fields["eyr"]) <= 2030)

        hgt = self.fields["hgt"]
        hgt = re.match("([0-9]{2,3})([a-z]{2})",  hgt)
        if hgt is not None and len(hgt.groups()) == 2:
            hgt = hgt.groups()
            hgt_number, hgt_unit = int(hgt[0]), hgt[1]
            hgt = (hgt_unit == "cm" and 150 <= hgt_number <= 193) or (
                hgt_unit == "in" and 59 <= hgt_number <= 76)
        else:
            hgt = False

        hcl = re.match(r"(^#[0-9a-f]{6}$)", self.fields["hcl"]) is not None
        ecl = self.fields["ecl"] in (
            "amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        pid = re.match(r"(^[0-9]{9}$)", self.fields["pid"]) is not None
        return byr and iyr and eyr and hgt and hcl and ecl and pid


def test():
    test_1 = PassportScanner("test_input_part1.txt")
    test_2 = PassportScanner("test_input_part2_1.txt")
    test_3 = PassportScanner("test_input_part2_2.txt")

    assert test_1.count_passports() == 2, "2 passports with required fields (p1)"
    assert test_2.count_validated_passports() == 0, "4 invalid passports inputted (p2)"
    assert test_3.count_validated_passports() == 3, "3 valid passports inputted (p2)"
    print("All tests passed")


def main():
    test()
    airport_scanner = PassportScanner("input.txt")
    part_1 = airport_scanner.count_passports()
    part_2 = airport_scanner.count_validated_passports()
    print("Part 1:", part_1)
    print("Part 2:", part_2)

    assert part_1 == 254, "Part 1 should be 254"
    assert part_2 == 184, "Part 2 should be 184"


if __name__ == "__main__":
    main()
