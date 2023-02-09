from random import choice

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789_-;'

with open('criptografia/num.txt', 'r') as arquivo: 
    for n in chars:
        char = choice(chars)
              