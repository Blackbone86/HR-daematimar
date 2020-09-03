age = int(input("Input age: ")) # Do not change this line

ticket_price = 40

if age >= 65:
    ticket_price *= 0.60
elif 5 < age < 20:
    ticket_price *= 0.80
elif age <= 5:
    ticket_price = 0
print(float(ticket_price))
