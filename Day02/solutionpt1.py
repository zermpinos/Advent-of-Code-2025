def solve():
    with open("input", "r") as f:
        line = f.read().strip()

    ranges = [r.strip() for r in line.split(",") if r.strip()]

    total = 0

    for r in ranges:
        lo, hi = map(int, r.split("-"))

        lo_len = len(str(lo))
        hi_len = len(str(hi))

        for length in range(lo_len, hi_len + 1):
            if length % 2 == 1:
                continue

            half = length // 2

            start = 10 ** (half - 1)
            end   = 10 ** half - 1

            for s in range(start, end + 1):
                n = int(str(s) + str(s))

                if n > hi:
                    break

                if n >= lo:
                    total += n

    print(total)


if __name__ == "__main__":
    solve()
