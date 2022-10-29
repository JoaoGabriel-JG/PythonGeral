import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

m = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
Iniciado = ['Planejado','Aguardando Subida','Acompanhando Produção','Em Ajuste Integrado','Desenvolvimento','Aplicar Integrado','Instalado Pré-Prod','Testes Integrado','Instalado Integrado','Aplicar Pacote Pre Prod','Impedimento']
Fechado = ['Done', 'Cancelado']
NaoIniciado = ['New', 'To Do']
Aguardando = ['Grooming', 'Em especificação']
Inf_Insuficientes = ['Revisão Especificação']
mat = np.zeros((12,5), dtype=np.int32)



with open('grafico/backlogGeral.csv', 'r') as csvfile:
    csv.field_size_limit(sys.maxsize)
    path = csv.reader(csvfile, delimiter=',')
    next(csvfile)

    for row in path:
        d = row[7]
        s = row[6]  

        
        data = datetime.strptime(d, '%d/%m/%Y %H:%M:%S') 
        
        if s in Iniciado:
            mat[data.month - 1, 0] += 1
        elif s in Fechado:
            mat[data.month - 1, 1] += 1
        elif s in NaoIniciado:
            mat[data.month -1, 2] += 1
        elif s in Aguardando:
            mat[data.month -1, 3] += 1
        else:
            mat[data.month - 1, 4] += 1

iniciado_qtd = [mat[0, 0], mat[1, 0], mat[2, 0], mat[3, 0], mat[4, 0], mat[5, 0], mat[6, 0], mat[7, 0], mat[8, 0], mat[9, 0], mat[10, 0], mat[11, 0]]
fechado_qtd = [mat[0, 1], mat[1, 1], mat[2, 1], mat[3, 1], mat[4, 1], mat[5, 1], mat[6, 1], mat[7, 1], mat[8, 1], mat[9, 1], mat[10, 1], mat[11, 1]]
naoIniciado_qtd = [mat[0, 2], mat[1, 2], mat[2, 2], mat[3, 2], mat[4, 2], mat[5, 2], mat[6, 2], mat[7, 2], mat[8, 2], mat[9, 2], mat[10, 2], mat[11, 2]]
aguardando_qtd = [mat[0, 3], mat[1, 3], mat[2, 3], mat[3, 3], mat[4, 3], mat[5, 3], mat[6, 3], mat[7, 3], mat[8, 3], mat[9, 3], mat[10, 3], mat[11, 3]]
inf_insuficiente_qtd = [mat[0, 4], mat[1, 4], mat[2, 4], mat[3, 4], mat[4, 4], mat[5, 4], mat[6, 4], mat[7, 4], mat[8, 4], mat[9, 4], mat[10, 4], mat[11, 4]]

fig, ax = plt.subplots()
ax.bar(m, iniciado_qtd, width = 0.3, label='Iniciado')
ax.bar(m, fechado_qtd, width=0.3, label='Fechado')
ax.bar(m, naoIniciado_qtd, width=0.3, label = 'Não iniciado')
ax.bar(m, aguardando_qtd, width=0.3, label = 'Aguardando inicio')
ax.bar(m, inf_insuficiente_qtd, width=0.3, label='Informações insuficientes')
ax.set_ylabel('Quantidade')
ax.set_title('Problemas separados por status e mês')
ax.legend()
plt.show()

