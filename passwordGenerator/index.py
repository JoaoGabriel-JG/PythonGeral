import random

print('Bem-vindo ao Gerador de Senhas')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&().,?0123456789'

number = int(input('Quantas senhas? '))

length = int(input('Quantos caracteres? '))

print('\nSuas senhas: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)