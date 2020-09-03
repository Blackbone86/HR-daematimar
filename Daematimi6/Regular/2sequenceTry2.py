n = int(input("Enter the length of the sequence: ")) # Do not change this line

num1 = 0
num2 = 0
num3 = 1
num_sum = 0

for i in range(n):
    num1 = num2
    num2 = num3
    num3 = num_sum
    num_sum = num1 + num2 + num3
    print(num_sum)
