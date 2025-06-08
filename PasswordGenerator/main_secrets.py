import secrets

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
length = 12

# Make sure that each category is present in password and append random choices from all characters
password = [secrets.choice(lowercase_letters), secrets.choice(uppercase_letters), secrets.choice(digits), secrets.choice(special_characters)]
for _ in range(length-len(password)):
    password += secrets.choice(all_characters)

# Shuffle to make random
shuffled_password = []
for i in range(len(password)):
    char = secrets.choice(password)
    password.remove(char)
    shuffled_password.append(char)

# Convert list to str and print
print(''.join(shuffled_password))
