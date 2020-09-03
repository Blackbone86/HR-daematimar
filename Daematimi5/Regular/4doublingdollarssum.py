max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))

# Fill in the missing code
total = 0
days_when_amount_acquired = 0
current_amount = 1
for i in range(1, max_days):
    if total >= target:
        break
    else:
        total += current_amount
        current_amount *= 2
        days_when_amount_acquired += 1
else:
    if total < target:
        days_when_amount_acquired = 0

print('Days needed:',days_when_amount_acquired)
