def parse_problem_columns(grid):
    h = len(grid)
    w = len(grid[0])

    blocks = []
    col = w - 1

    while col >= 0:
        if all(grid[r][col] == " " for r in range(h)):
            col -= 1
            continue
        end = col + 1
        while col >= 0 and not all(grid[r][col] == " " for r in range(h)):
            col -= 1
        start = col + 1
        blocks.append((start, end))
    return blocks

def extract_problem(grid, start, end):
    h = len(grid)
    operator_row = None

    for r in range(h):
        cell = grid[r][start:end].strip()
        if cell in ("+", "*"):
            operator_row = r

    num_rows = []
    for r in range(operator_row):
        snippet = grid[r][start:end].strip()
        if snippet.isdigit():
            num_rows.append(snippet)

    width = end - start
    columns = [[] for _ in range(width)]

    for r in range(operator_row):
        row_slice = grid[r][start:end]
        for i, ch in enumerate(row_slice):
            if ch.isdigit():
                columns[i].append(ch)

    numbers = []
    for col_digits in columns:
        if col_digits:
            numbers.append(int("".join(col_digits)))
    operator = grid[operator_row][start:end].strip()
    return numbers, operator

def compute_total(grid):
    blocks = parse_problem_columns(grid)
    total = 0
    for start, end in blocks:
        numbers, op = extract_problem(grid, start, end)
        if op == "+":
            val = sum(numbers)
        else:
            val = 1
            for n in numbers:
                val *= n
        total += val
    return total

def main():
    with open("input") as f:
        raw = [line.rstrip("\n") for line in f]
    width = max(len(line) for line in raw)
    grid = [line.ljust(width) for line in raw]
    result = compute_total(grid)
    print("Grand total:", result)

if __name__ == "__main__":
    main()
