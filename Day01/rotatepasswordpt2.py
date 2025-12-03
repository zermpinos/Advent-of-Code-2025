def count_zero_hits_2(filename):
    pos = 50
    count = 0

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            steps = int(line[1:])

            # +1 for R, -1 for L
            delta = 1 if direction == "R" else -1

            for _ in range(steps):
                pos = (pos + delta) % 100
                if pos == 0:
                    count += 1

    return count


print(count_zero_hits_2("input"))
