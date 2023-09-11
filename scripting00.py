def triangle(base, character):
    for i in range(1 - base % 2, base, 2):
        print((base - i - 1) // 2 * ' ' + (i + 1) * character + (base - i - 1) // 2 * ' ')

triangle(7, 'X')