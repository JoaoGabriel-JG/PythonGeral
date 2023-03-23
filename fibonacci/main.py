print ('-' *30)
print (' ' *3, 'Sequência de Fibonacci')
print ('-' *30)

fibonacci = [0, 1]

valor = int(input('Insira um número: '))  

while valor > int(*fibonacci[-1:]):   
    n1 = fibonacci[-2:][0]
    n2 = int(*fibonacci[-1:])

    fibonacci.append(n1 + n2)

    if valor in fibonacci:             
        print([n for n in fibonacci])
        print(f'O valor {valor} está dentro da Fibonacci')
        break    
    elif valor < int(*fibonacci[-1:]):    
        print('O valor não pertence a Fibonacci')
        break