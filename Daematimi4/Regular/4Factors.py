n = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below
current_factor_num = 1

while current_factor_num <= n:
    if n % current_factor_num == 0:
        print(current_factor_num)
    current_factor_num += 1
