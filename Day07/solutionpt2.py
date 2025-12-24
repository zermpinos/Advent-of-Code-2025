def count_timelines(text):
    with open(text, 'r') as f:
        grid = [line.rstrip('\n') for line in f]

    h = len(grid)
    w = len(grid[0])
    memo = {}

    def dfs(a, b):
        if b >= h:
            return 1  # beam exits, counts as 1 timeline
        if grid[b][a] == '^':
            total = 0
            if a > 0:
                total += dfs(a - 1, b + 1)
            if a < w - 1:
                total += dfs(a + 1, b + 1)
            return total
        
        # continue downward; use memoization to avoid recomputation
        if (a, b + 1) not in memo:
            memo[(a, b + 1)] = dfs(a, b + 1)
        return memo[(a, b + 1)]

    # find starting point 'S'
    for y, row in enumerate(grid):
        if 'S' in row:
            start_x = row.index('S')
            start_y = y
            break
    else:
        raise ValueError("Starting point 'S' not found in the grid.")

    return dfs(start_x, start_y)

if __name__ == "__main__":
    filename = "input"
    answer = count_timelines(filename)
    print(answer)
