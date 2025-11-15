def count_digit_3(N: int) -> int:
    """
    1..N gacha barcha sonlarda raqam '3' necha marta uchraydi.
    """
    d = 3
    factor = 1
    count = 0
    while factor <= N:
        higher = N // (factor * 10)
        current = (N // factor) % 10
        lower = N % factor

        count += higher * factor
        if current > d:
            count += factor
        elif current == d:
            count += lower + 1

        factor *= 10

    return count

print(count_digit_3(33))
print(count_digit_3(3))
print(count_digit_3(100))
