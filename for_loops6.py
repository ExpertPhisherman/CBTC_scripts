s = 0
for i in range(3, 5000):
    if (i % 5 == 0) ^ (i % 7 == 0):
        s += i
print(s)