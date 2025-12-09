def merge_ranges(ranges):
    if not ranges:
        return []

    ranges.sort()
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def count_total_fresh_ids(ranges):
    merged = merge_ranges(ranges)
    total = 0
    for start, end in merged:
        total += (end - start + 1)
    return total


def main():
    ranges = []
    with open("input", "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            a, b = map(int, line.split("-"))
            ranges.append((a, b))

    print(count_total_fresh_ids(ranges))


if __name__ == "__main__":
    main()
