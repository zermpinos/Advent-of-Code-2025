def max_number_from_bank(bank: str, k: int) -> int:
    stack = []
    n = len(bank)
    to_remove = n - k

    for digit in bank:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    final_digits = stack[:k]
    return int("".join(final_digits))


def solve():
    with open("input", "r") as f:
        banks = [line.strip() for line in f if line.strip()]

    total = 0
    k = 12

    for bank in banks:
        total += max_number_from_bank(bank, k)

    print(total)


if __name__ == "__main__":
    solve()
  
