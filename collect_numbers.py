def input_Loop():
    numbers_list = []
    n = int(input('How many numbers will you enter? '))
    for i in range(n):
        numbers_list += [int(input(f'Enter a number ({i + 1} of {n}): '))]
    numbers_list.sort()
    print(numbers_list)

input_Loop()