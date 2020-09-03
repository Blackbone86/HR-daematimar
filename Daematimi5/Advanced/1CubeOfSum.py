import math
max_num = int(input("Input maximum number: "))
total = 0
for i in range(1, max_num + 1):
    for number in str(i):
        total += int(number)
    if total**3 == i:
        print(i)
    else:
        total = 0
