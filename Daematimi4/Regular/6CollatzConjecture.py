a0 = int(input("Input a positive int: "))   # Do not change this line


while a0 != 1:
    if a0 % 2 == 0:
        a0 /= 2
    elif a0 % 1 == 0:
        a0 = (3 * a0) + 1
    print(int(a0))
