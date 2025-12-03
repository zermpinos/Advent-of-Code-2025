def is_repeated_number(n: int) -> bool:
    s = str(n)
    length = len(s)
    for l in range(1, length // 2 + 1):
        if length % l == 0:
            reps = length // l
            if reps >= 2 and s == s[:l] * reps:
                return True
    return False


def solve():
    with open("input", "r") as f:
        line = f.read().strip()

    ranges = [r.strip() for r in line.split(",") if r.strip()]
    total = 0

    for r in ranges:
        lo, hi = map(int, r.split("-"))
        for n in range(lo, hi + 1):
            if is_repeated_number(n):
                total += n

    print(total)


if __name__ == "__main__":
    solve()
