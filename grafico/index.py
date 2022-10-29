import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

M = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
iniciado = ['Planejado', 'Aguardando Subida', 'Acompanhando Prodção', 'Em Ajuste', 'Integrado',
            'Desenvolvimento', 'Aplicar Integrado','Instalado Pré-Prod', 'Testes Integrado', 'Instalando Integrado',
            'Aplicar Pacote Pré-Prod', 'Impedimento']
fechado = ['Done', 'Cancelado']
naoIniciado = ['New', 'To Do']
aguardando = ['Grooming', 'Em Especificação']
informaInsu = ['Revisão Especificação']
mat = np.zeros

with open('backlogGeral.csv') as csvfile:
    csv.field_size_limit(sys.maxsize)
    path = csv.reader(csvfile, delimiter = ',')
    next(csvfile)

    for row in path:
        d = row[7]
        s = row[6]

        data = datetime.strptime(d, '%d/%m/%Y %H:%M:%S')

        if s in iniciado:
            
