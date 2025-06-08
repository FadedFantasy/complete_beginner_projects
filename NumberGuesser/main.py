import random

rand_num = random.randint(1, 10)
print('The computer generated a number between 1 and 10. Try to guess it!')

nb_guesses = 0
while True:
    user_guess = input('Your guess: ')

    # filter wrong user input
    if not user_guess.isdigit():
        print('Wrong input! Please input an integer number between 1 and 10')
        continue
    if not 1 <= int(user_guess) <= 10:
        print('Wrong input! Please input an integer number between 1 and 10')
        continue

    nb_guesses += 1

    if int(user_guess) == rand_num:
        print(f'You guessed correctly! It took you {nb_guesses} attempts.\n')
        break
    else:
        print('Unfortunately this was not correct :( Try again!')
