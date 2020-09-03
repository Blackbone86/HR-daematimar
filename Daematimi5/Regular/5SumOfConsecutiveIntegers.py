num = int(input("Input an int: ")) # Do not change this line
sumtotal = 0
for i in range(1,num+1):
    for j in range(1,i+1):
        sumtotal += j
    print(sumtotal)
    sumtotal = 0


total2 = 0
for i in range(1, num + 1):
    total2 += i
    print(total2)