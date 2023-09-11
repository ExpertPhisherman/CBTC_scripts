def is_int(char):
    return str(char).isnumeric()

def is_vow(char):
    return str(char).lower() in 'aeiou'

def is_con(char):
    return str(char).lower() in 'bcdfghjklmnpqrstvwxyz'

random_data = open('random.txt').read()
ints = 0
vows = 0
cons = 0
for char in random_data:
    if is_int(char):
        ints += 1
    elif is_vow(char):
        vows += 1
    elif is_con(char):
        cons += 1
print((cons + vows) * ints)