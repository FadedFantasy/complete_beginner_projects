def is_number(value):
    """Checks if a value is a number and returns a bool"""
    try:
        float(value)
        return True
    except ValueError:
        return False


while True:
    calc_type = input('Which calculation would you like to perform? Addition (a), Subtraction (b), Multiplication (c), Division (d): ')

    if calc_type not in ['a', 'b', 'c', 'd']:
        print('Please enter a valid option! Valid options are a, b, c, d')
        continue

    nb1 = input('Type in the first number: ')
    while not is_number(nb1):
        print('Please type a number for the first number!')
        nb1 = input('Type in the first number: ')

    nb2 = input('Type in the second number: ')
    while not is_number(nb2):
        print('Please type a number for the second number!')
        nb2 = input('Type in the second number: ')

    nb1 = float(nb1)
    nb2 = float(nb2)

    result = ''
    if calc_type == 'a':
        result = nb1 + nb2
    elif calc_type == 'b':
        result = nb1 - nb2
    elif calc_type == 'c':
        result = nb1 * nb2
    elif calc_type == 'd':
        result = nb1 / nb2

    print('Your result is', result)
