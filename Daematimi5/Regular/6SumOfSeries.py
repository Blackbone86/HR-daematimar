length = int(input("Input the length of series: "))

negative = False
total = 0

for i in range(1, length + 1):

    if not negative:
        print(i * 2)
        negative = True
        total += i * 2
        continue

    if negative:
        print(-i * 2)
        negative = False
        total += -i * 2
        continue

print(f"Sum: {total}")
