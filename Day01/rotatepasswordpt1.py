def count_zero_hits(filename):
    pos = 50
    count = 0

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            if direction == "L":
                pos = (pos - distance) % 100
            else:  # "R"
                pos = (pos + distance) % 100

            if pos == 0:
                count += 1

    return count


print(count_zero_hits("input"))
