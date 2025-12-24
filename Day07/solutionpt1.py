def count_splits(grid):
    h = len(grid)
    w = len(grid[0])

    start = None
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'S':
                start = (r, c)
                break
        if start:
            break

    beams = [(start[0] + 1, start[1])]
    split_count = 0

    hit_splitter = set()  # track which splitters we've already counted

    while beams:
        new_beams = []

        for br, bc in beams:
            r, c = br, bc

            while 0 <= r < h:
                cell = grid[r][c]

                if cell == '^':
                    if (r, c) not in hit_splitter:
                        hit_splitter.add((r, c))
                        split_count += 1

                        if c - 1 >= 0:
                            new_beams.append((r + 1, c - 1))
                        if c + 1 < w:
                            new_beams.append((r + 1, c + 1))

                    break

                r += 1

        beams = new_beams

    return split_count


def main():
    with open("input", "r") as f:
        grid = [line.rstrip("\n") for line in f]

    print(count_splits(grid))


if __name__ == "__main__":
    main()
