from random import choice
import json

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789_-;'
dictionary = {}

with open('criptografia/num.txt', 'r') as arquivo: 
    numero = arquivo.readlines()
    for n in numero:
        char = choice(chars)
        chars = chars.replace(char, '')
        n = n.replace('\n', '')
        dictionary.update({ char: n })

print(dictionary)

# with open('leozinhoPVP.json', 'w') as arquivo:
#     json.dump(dictionary, arquivo, ensure_ascii=False, indent=2)
