'''
def main_once():
    if input('Input your name: ') != 'Bob':
        print('Access Denied: User Not Found')
        return
    if input('Enter a password: ') != 'pass1234':
        print('Access Denied: Incorrect Password')
        return
    print('Access Granted')
main_once()
'''

'''
def main_loop():
    while input('Input your name: ') != 'Bob':
        print('Access Denied: User Not Found')
    while input('Enter a password: ') != 'pass1234':
        print('Access Denied: Incorrect Password')
    print('Access Granted')
main_loop()
'''

def main_three():
    if input('Input your name: ') != 'Bob':
        print('User Not Found')
        return
    for i in range(3):
        if input('Enter a password: ') == 'pass1234':
            print('Access Granted')
            return
    print('Access Denied')
main_three()