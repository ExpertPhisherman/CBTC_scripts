def C_FK(c):
    f = 1.8 * c + 32
    k = c + 273.15
    return f, k

print('Welcome to the Temperature Conversion Program!')
c = float(input('Input a temperature in Celcius: '))
f, k = C_FK(c)
print(f'The temperature {c}C is equal to {f}F and {k}K.')