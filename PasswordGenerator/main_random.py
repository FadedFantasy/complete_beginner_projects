import random

# Define all characters and all per category
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
                      '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
                      '_', '`', '{', '|', '}', '~']
all_characters = lowercase_letters + uppercase_letters + digits + special_characters

# Define length of password
length = 8

# Make sure that each category is present in password and append random choices from all characters
password = [random.choice(lowercase_letters), random.choice(uppercase_letters), random.choice(digits), random.choice(special_characters)]

for i in range(length - len(password)):
    password = password + [(random.choice(all_characters))]

# Shuffle to make random OPTIONAL
random.shuffle(password)

# convert list to str and print
print(''.join(password))
