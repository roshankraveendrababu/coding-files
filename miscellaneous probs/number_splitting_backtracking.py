def S_number_check(sqrt_value, digits):
    if digits < sqrt_value:
        return False
    if digits == sqrt_value:
        return True

    magnitude = 10
    while magnitude < digits:
        remaining_digits, split_digits = divmod(digits, magnitude)
        if split_digits >= sqrt_value:
            return False
        if S_number_check(sqrt_value - split_digits, remaining_digits):
            return True
        magnitude *= 10

    return False

print(S_number_check(1296,1679616))
