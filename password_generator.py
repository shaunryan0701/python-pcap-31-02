import random 

alpha = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
special = '!@#$%^&*()_+'

def print_instructions():
  print('''
-- Password generato --
Choose option:
1. generate password
2. exit the program
''')

def generate_password():
  length = int(input('Provide password length: '))
  digits = input("Use digits? (y/n): ")
  upper = input('Use uppercase letters? (y/n): ')
  special_char = input('Use special characters? (y/n): ')
  print('\n')

  password_string = ''
  password_list = alpha

  if digits == 'y':
    password_list += numbers

  if special_char == 'y': 
    password_list += special

  for _ in range(length):
    new_char = random.choice(password_list)
    if new_char.isalpha() and upper == 'y':
      if random.randint(0,1) == 1:
        new_char = new_char.upper()
    password_string += new_char

  return password_string

print_instructions()  
choice = input('Your choice: ')

while choice != '2':
  if choice == '1':
      print('Generated password: ', generate_password(),'\n')
  else:
    print('Please enter a correct value')
  print_instructions()  
  choice = input('Your choice: ')

print('Bye!')
