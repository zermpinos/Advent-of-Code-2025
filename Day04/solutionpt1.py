def count_accessible_rolls(grid):
    h = len(grid)
    w = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1),
    ]

    def neighbor_count(r, c):
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w:
                if grid[nr][nc] == '@':
                    count += 1
        return count

    total = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] == '@' and neighbor_count(r, c) < 4:
                total += 1
    return total


def main():
    with open("input", "r") as f:
        grid = [line.strip() for line in f if line.strip()]

    answer = count_accessible_rolls(grid)
    print(answer)


if __name__ == "__main__":
    main()
