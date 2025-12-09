def parse_ranges_and_ids(lines):
    ranges = []
    ids = []
    section = 0

    for line in lines:
        line = line.strip()
        if line == "":
            section = 1
            continue

        if section == 0:
            lo, hi = map(int, line.split("-"))
            ranges.append((lo, hi))
        else:
            ids.append(int(line))

    return ranges, ids


def is_fresh(ingredient_id, ranges):
    for lo, hi in ranges:
        if lo <= ingredient_id <= hi:
            return True
    return False


def count_fresh_ids(ranges, ids):
    return sum(1 for x in ids if is_fresh(x, ranges))


def main():
    with open("input", "r") as f:
        lines = f.readlines()

    ranges, ids = parse_ranges_and_ids(lines)
    answer = count_fresh_ids(ranges, ids)

    print(answer)


if __name__ == "__main__":
    main()
