def solve():
    with open("input", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    total = 0

    for line in lines:
        max_joltage = 0
        n = len(line)
        # Try all pairs i < j
        for i in range(n):
            for j in range(i + 1, n):
                joltage = int(line[i] + line[j])
                if joltage > max_joltage:
                    max_joltage = joltage
        total += max_joltage

    print(total)

if __name__ == "__main__":
    solve()
  
