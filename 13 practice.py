count_ticket = int(input('How many tickets?'))
price = 0
for a in range(count_ticket):
    age = int(input('How old?'))
    if age < 18:
        print('Free')
    elif 18 <= age <= 25:
        price += 990
        print(price, 'rub')
    else:
        price += 1390
        print(price, 'rub')
if count_ticket >3:
    print('All cost with discount ', round(price) * 1.1, 'rub')
else:
    print('All cost', round(price), 'rub')