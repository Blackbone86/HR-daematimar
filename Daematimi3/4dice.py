d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

if not (d1 in range(1,7) and d2 in range(1,7)):
    print("Invalid input")
elif d1 == d2:
    print("Pair")
else:
    print(d1+d2)