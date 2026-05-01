negative = []
positive = []
val = 0

while True:
    try:
        raw_val = input('Enter your number, or \'done\' to finish ==> ')
        val = int(raw_val)
        if val<0:
            negative.append(val)
        else:
            positive.append(val)
    except ValueError:
        val = str(raw_val)
        if val == 'done':
            break
        else: print('please enter a whole number or \'done\' to finish')

sum_positive = 0
sum_negative = 0
for num in positive:
    sum_positive+=num

for num in negative:
    sum_negative+=num
    
print(f'The sum of your negative numbers is {sum_negative}')
print(f'The sum of your positive numbers is {sum_positive}')
