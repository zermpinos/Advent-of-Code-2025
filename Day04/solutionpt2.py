def count_neighbors(grid, r, c):
    h = len(grid)
    w = len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1),
    ]
    cnt = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '@':
            cnt += 1
    return cnt


def remove_all(grid):
    total_removed = 0
    h, w = len(grid), len(grid[0])

    grid = [list(row) for row in grid]

    while True:
        to_remove = []

        for r in range(h):
            for c in range(w):
                if grid[r][c] == '@':
                    if count_neighbors(grid, r, c) < 4:
                        to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = '.'

        total_removed += len(to_remove)

    return total_removed


def main():
    with open("input", "r") as f:
        grid = [line.strip() for line in f if line.strip()]

    answer = remove_all(grid)
    print(answer)


if __name__ == "__main__":
    main()
