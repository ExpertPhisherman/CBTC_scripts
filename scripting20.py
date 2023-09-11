def is_valid(password):
    valid = True

    has_cap = False
    for char in password:
        if char.isupper():
            has_cap = True
    valid = has_cap

    for char in password:
        if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@:&':
            valid = False

    if len(password) < 4 or len(password) > 20:
        valid = False

    if 'admin' in password.lower() or 'root' in password.lower() or 'password' in password.lower():
        valid = False

    return valid

passwords = open('passwords.txt').read().split(',')
#print(passwords)

fails = 0
for password in passwords:
    if not is_valid(password):
        fails += 1
print(fails)