max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))

# Fill in the missing code
days_when_amount_acquired = 0
current_money = 1
for i in range(max_days):
    if current_money >= target:
        break
    else:
        current_money *= 2
        days_when_amount_acquired += 1
else:
    if current_money <= target:
        days_when_amount_acquired = 0

print('Days needed:',days_when_amount_acquired)
