def merry_christmas(height):
    for i in range(height):
        spaces = " " * (height - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

    trunk_width = height // 3 if height > 3 else 1
    trunk_height = height // 5 if height > 5 else 1
    trunk = " " * (height - trunk_width // 2 - 1) + "*" * trunk_width
    for _ in range(trunk_height):
        print(trunk)

merry_christmas(20)