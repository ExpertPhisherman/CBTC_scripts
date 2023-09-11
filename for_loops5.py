my_list = list()
for i in range(1,5050505,23):
    my_list.append(i)

s = 0
for i in my_list:
    if i % 2:
        s += i
print(s)