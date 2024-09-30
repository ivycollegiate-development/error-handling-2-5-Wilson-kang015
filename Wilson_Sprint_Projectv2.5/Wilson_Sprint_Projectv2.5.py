try:
    number_value = int(input('Please enter a number: '))
except ValueError:
    print('Sorry, but that is not a vaild number.')

print(f'The number that you imput: {number_value}')