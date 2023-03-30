from funcionario import Funcionario

funcionario = Funcionario('Leonardo', 'LeonardoOS14@gmail.com')

funcionario.cadastro_hora('Jan', 300)
funcionario.cadastro_hora('Fev', 200)
funcionario.cadastro_salario_hora('Jan', 5)
funcionario.cadastro_salario_hora('Fev', 5)
print(funcionario)
print(funcionario.calcula_salario('Jan'))
print(funcionario.calcula_salario('Fev'))
