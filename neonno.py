def is_neon_number(n):
    square = n * n
    digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == n

# Example usage:
for num in range(0, 101):
    if is_neon_number(num):
        print(num, "is a neon number.")