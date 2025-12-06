def digitlist_to_number(l: list[int]) -> int:
    accum = 0
    for digit in l:
        accum *= 10
        accum += digit
    return accum
