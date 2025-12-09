def parse_problems(grid):
    h = len(grid)
    w = len(grid[0])

    problems = []
    col = 0

    while col < w:
        if all(grid[r][col] == ' ' for r in range(h)):
            col += 1
            continue

        start = col
        while col < w and not all(grid[r][col] == ' ' for r in range(h)):
            col += 1

        problems.append((start, col))  # (start, end)
    return problems


def extract_problem(grid, start, end):
    h = len(grid)
    operator_row = None
    for r in range(h):
        stripped = grid[r][start:end].strip()
        if stripped in ("+", "*"):
            operator_row = r
            
    if operator_row is None:
        raise ValueError("No operator found in problem block!")

    numbers = []
    for r in range(operator_row):
        stripped = grid[r][start:end].strip()
        if stripped.isdigit():
            numbers.append(int(stripped))

    op = grid[operator_row][start:end].strip()
    return numbers, op


def compute_worksheet_total(grid):
    problems = parse_problems(grid)
    total = 0

    for start, end in problems:
        numbers, op = extract_problem(grid, start, end)

        if op == "+":
            value = sum(numbers)
        else:  # "*"
            value = 1
            for n in numbers:
                value *= n

        total += value

    return total


def main():
    with open("input") as f:
        lines = [line.rstrip("\n") for line in f]

    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    total = compute_worksheet_total(grid)
    print("Grand total:", total)


if __name__ == "__main__":
    main()
